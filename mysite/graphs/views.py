from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import PancreasTumorPro, ScrapedColonPro, WholePancreasPro, ColonTumorPro, AllProPhos
from plotly.offline import plot
import plotly.graph_objects as go
from django.http import HttpRequest
from django.db.models import Q

# Create your views here.


def search(request):
    return render(request, "graphs/search.html")


def search_results(request):

    query = request.GET.get('user_input')

    if query and request.method == 'GET':
        all_pro = AllProPhos.objects.filter(
            Q(protein_id__icontains=query) | Q(
                gene_symbol__icontains=query) | Q(description__icontains=query))
        context = {
            'all_pro': all_pro
        }
    else:
        all_pro = AllProPhos.objects.all()
        context = {
            'all_pro': all_pro
        }

    return render(request, "graphs/search_results.html", context)


def graphs(request, id):
    # protein/gene info
    all_pro = AllProPhos.objects.get(id=id)
    gene_symbol = all_pro.gene_symbol
    description = all_pro.description
    protein_id = all_pro.protein_id

    try:
        pancreas_tumor_pro = PancreasTumorPro.objects.get(id=id)
        pancreas_tumor_pro_pdx_1 = pancreas_tumor_pro.pdx_1
        pancreas_tumor_pro_pdx_2 = pancreas_tumor_pro.pdx_2
        pancreas_tumor_pro_pdx_3 = pancreas_tumor_pro.pdx_3
        pancreas_tumor_pro_pdxp53_1 = pancreas_tumor_pro.pdxp53_1
        pancreas_tumor_pro_pdxp53_2 = pancreas_tumor_pro.pdxp53_2
        pancreas_tumor_pro_pdxp53_3 = pancreas_tumor_pro.pdxp53_3
        pancreas_tumor_pro_d314 = pancreas_tumor_pro.d314
        pancreas_tumor_pro_d693 = pancreas_tumor_pro.d693
        pancreas_tumor_pro_d705 = pancreas_tumor_pro.d705
        pancreas_tumor_pro_d751 = pancreas_tumor_pro.d751
        pancreas_tumor_pro_d756 = pancreas_tumor_pro.d756
        pancreas_tumor_pro_average_norm_wt = pancreas_tumor_pro.average_norm_wt
        pancreas_tumor_pro_average_norm_g12d = pancreas_tumor_pro.average_norm_g12d
        pancreas_tumor_pro_average_norm_g12d_average_norm_wt = pancreas_tumor_pro.average_norm_g12d_average_norm_wt
    except PancreasTumorPro.DoesNotExist:
        pancreas_tumor_pro = None

    try:
        scraped_colon_pro = ScrapedColonPro.objects.get(id=id)
        scraped_colon_pro_fabp_1 = scraped_colon_pro.norm_fabp_1
        scraped_colon_pro_fabp_2 = scraped_colon_pro.norm_fabp_2
        scraped_colon_pro_fabp_4 = scraped_colon_pro.norm_fabp_4
        scraped_colon_pro_fabp_5 = scraped_colon_pro.norm_fabp_5
        scraped_colon_pro_g12d_1 = scraped_colon_pro.norm_2171_g12d_1
        scraped_colon_pro_g12d_2 = scraped_colon_pro.norm_2172_g12d_2
        scraped_colon_pro_g12d_3 = scraped_colon_pro.norm_g12d_3
        scraped_colon_pro_g12d_4 = scraped_colon_pro.norm_g12d_4
        scraped_colon_pro_average_norm_wt = scraped_colon_pro.average_norm_wt
        scraped_colon_pro_average_norm_g12d = scraped_colon_pro.average_norm_g12d
        scraped_colon_pro_average_norm_g12d_average_norm_wt = scraped_colon_pro.average_norm_g12d_average_norm_wt
    except ScrapedColonPro.DoesNotExist:
        scraped_colon_pro = None

    try:
        whole_pancreas_pro = WholePancreasPro.objects.get(id=id)
        whole_pancreas_pro_wt_1 = whole_pancreas_pro.norm_wt_1
        whole_pancreas_pro_wt_2 = whole_pancreas_pro.norm_wt_2
        whole_pancreas_pro_wt_3 = whole_pancreas_pro.norm_wt_3
        whole_pancreas_pro_wt_4 = whole_pancreas_pro.norm_wt_4
        whole_pancreas_pro_g12d_1 = whole_pancreas_pro.norm_g12d_1
        whole_pancreas_pro_g12d_2 = whole_pancreas_pro.norm_g12d_2
        whole_pancreas_pro_g12d_3 = whole_pancreas_pro.norm_g12d_3
        whole_pancreas_pro_average_norm_wt = whole_pancreas_pro.average_norm_wt
        whole_pancreas_pro_average_norm_g12d = whole_pancreas_pro.average_norm_g12d
        whole_pancreas_pro_average_norm_g12d_average_norm_wt = whole_pancreas_pro.average_norm_g12d_average_norm_wt
    except WholePancreasPro.DoesNotExist:
        whole_pancreas_pro = None

    try:
        colon_tumor_pro = ColonTumorPro.objects.get(id=id)
        colon_tumor_pro_control1 = colon_tumor_pro.control1
        colon_tumor_pro_control2 = colon_tumor_pro.control2
        colon_tumor_pro_control3 = colon_tumor_pro.control3
        colon_tumor_pro_control4 = colon_tumor_pro.control4
        colon_tumor_pro_control5 = colon_tumor_pro.control5
        colon_tumor_pro_kras1 = colon_tumor_pro.kras1
        colon_tumor_pro_kras2 = colon_tumor_pro.kras2
        colon_tumor_pro_kras3 = colon_tumor_pro.kras3
        colon_tumor_pro_kras4 = colon_tumor_pro.kras4
        colon_tumor_pro_kras5 = colon_tumor_pro.kras5
        colon_tumor_pro_average_norm_wt = colon_tumor_pro.average_norm_wt
        colon_tumor_pro_average_norm_g12d = colon_tumor_pro.average_norm_g12d
        colon_tumor_pro_average_norm_g12d_average_norm_wt = colon_tumor_pro.average_norm_g12d_average_norm_wt
    except ColonTumorPro.DoesNotExist:
        colon_tumor_pro = None

    def box_colon():

        layout = dict(
            title=gene_symbol,
            template="plotly_white",
        )
        fig = go.Figure(layout=layout)
        fig.update_xaxes(tickangle=45)
        # scraped colon protein
        try:
            scp_wt = [scraped_colon_pro_fabp_1, scraped_colon_pro_fabp_2,
                      scraped_colon_pro_fabp_4, scraped_colon_pro_fabp_5]
            scp_g12d = [scraped_colon_pro_g12d_1, scraped_colon_pro_g12d_2,
                        scraped_colon_pro_g12d_3, scraped_colon_pro_g12d_4]
            fig.add_trace(go.Box(x=['CE WT', 'CE WT', 'CE WT', 'CE WT'], y=scp_wt, name='Colonic epithelium WT (CE WT)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
            fig.add_trace(go.Box(x=['CE G12D', 'CE G12D', 'CE G12D', 'CE G12D'], y=scp_g12d, name='Colonic epithelium G12D (CE G12D)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
        except:
            fig.add_trace(go.Box(y=[], name='Colonic epithelium WT'))
            fig.add_trace(go.Box(y=[], name='Colonic epithelium G12D'))
        # colon tumor protein
        try:
            ctp_wt = [colon_tumor_pro_control1, colon_tumor_pro_control2,
                      colon_tumor_pro_control3, colon_tumor_pro_control4, colon_tumor_pro_control5]
            ctp_g12d = [colon_tumor_pro_kras1, colon_tumor_pro_kras2,
                        colon_tumor_pro_kras3, colon_tumor_pro_kras4, colon_tumor_pro_kras5]
            fig.add_trace(go.Box(x=['CT WT', 'CT WT', 'CT WT', 'CT WT', 'CT WT'], y=ctp_wt, name='Apc-mutant colon WT (CT WT)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
            fig.add_trace(go.Box(x=['CT G12D', 'CT G12D', 'CT G12D', 'CT G12D', 'CT G12D'], y=ctp_g12d, name='Apc-mutant colon G12D (CT G12D)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
        except:
            fig.add_trace(go.Box(y=[], name='Apc-mutant colon WT'))
            fig.add_trace(go.Box(y=[], name='Apc-mutant colon G12D'))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def box_pancreas():

        layout = dict(
            title=gene_symbol,
            template="plotly_white",
        )
        fig = go.Figure(layout=layout)
        fig.update_xaxes(tickangle=45)
        # pancreas tumor protein
        try:
            ptp_wt = [pancreas_tumor_pro_pdx_1,
                      pancreas_tumor_pro_pdx_2, pancreas_tumor_pro_pdx_3,
                      pancreas_tumor_pro_pdxp53_1, pancreas_tumor_pro_pdxp53_2,
                      pancreas_tumor_pro_pdxp53_3]
            ptp_g12d = [pancreas_tumor_pro_d314, pancreas_tumor_pro_d693,
                        pancreas_tumor_pro_d705, pancreas_tumor_pro_d751, pancreas_tumor_pro_d756]
            fig.add_trace(go.Box(x=['PT WT', 'PT WT', 'PT WT', 'PT WT', 'PT WT', 'PT WT'], y=ptp_wt, name='Tp53-mutant pancreas WT (PT WT)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
            fig.add_trace(go.Box(x=['PT G12D', 'PT G12D', 'PT G12D', 'PT G12D', 'PT G12D'], y=ptp_g12d, name='Tp53-mutant pancreas G12D (PT G12D)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
        except:
            fig.add_trace(go.Box(y=[], name='Tp53-mutant pancreas WT'))
            fig.add_trace(go.Box(y=[], name='Tp53-mutant pancreas G12D'))
        # whole pancreas protein
        try:
            wpp_wt = [whole_pancreas_pro_wt_1, whole_pancreas_pro_wt_2,
                      whole_pancreas_pro_wt_3, whole_pancreas_pro_wt_4]
            wpp_g12d = [whole_pancreas_pro_g12d_1,
                        whole_pancreas_pro_g12d_2, whole_pancreas_pro_g12d_3]
            fig.add_trace(go.Box(x=['WP WT', 'WP WT', 'WP WT', 'WP WT'], y=wpp_wt, name='Whole pancreas WT (WP WT)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
            fig.add_trace(go.Box(x=['WP G12D', 'WP G12D', 'WP G12D'], y=wpp_g12d, name='Whole pancreas G12D (WP G12D)',
                                 marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
        except:
            fig.add_trace(go.Box(y=[], name='Whole pancreas WT'))
            fig.add_trace(go.Box(y=[], name='Whole pancreas G12D'))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def scatter_colon():
        layout = dict(
            title="Average G12D/Average WT",
            template="plotly_white",
            # paper_bgcolor="rgba(0,0,0,0)",
            # plot_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=False, zeroline=True,
                       showline=True),
            xaxis=dict(showgrid=False, showline=True, rangemode='tozero'),
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        fig.add_shape(go.layout.Shape(type="line", x0=1, x1=1,
                                      y0=0, y1=1, line=dict(color="#d62728", width=1.5, dash='dot')))
        fig.update_shapes(dict(xref='x'))
        try:
            ctp_ratio = colon_tumor_pro_average_norm_g12d_average_norm_wt
            fig.add_trace(go.Scatter(
                x=[ctp_ratio], y=['Apc-mutant colon'], mode="markers"))
        except:
            test = 0
        try:
            scp_ratio = scraped_colon_pro_average_norm_g12d_average_norm_wt
            fig.add_trace(go.Scatter(
                x=[scp_ratio], y=['Colonic epithelium'], mode="markers"))
        except:
            test = 0
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def scatter_pancreas():
        layout = dict(
            title="Average G12D/Average WT",
            template="plotly_white",
            # paper_bgcolor="rgba(0,0,0,0)",
            # plot_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=False, zeroline=True,
                       showline=True),
            xaxis=dict(showgrid=False, showline=True, rangemode='tozero'),
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        fig.add_shape(go.layout.Shape(type="line", x0=1, x1=1,
                                      y0=0, y1=1, line=dict(color="#d62728", width=1.5, dash='dot')))
        fig.update_shapes(dict(xref='x'))
        try:
            ptp_ratio = pancreas_tumor_pro_average_norm_g12d_average_norm_wt
            fig.add_trace(go.Scatter(
                x=[ptp_ratio], y=['Tp53-mutant pancreas'], mode="markers"))
        except:
            test = 0
        try:
            wpp_ratio = whole_pancreas_pro_average_norm_g12d_average_norm_wt
            fig.add_trace(go.Scatter(
                x=[wpp_ratio], y=['Whole pancreas'], mode="markers"))
        except:
            test = 0
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'box_colon': box_colon(),
        'box_pancreas': box_pancreas(),
        'gene_symbol': gene_symbol,
        'all_pro': all_pro,
        'scatter_colon': scatter_colon(),
        'scatter_pancreas': scatter_pancreas()

    }
    return render(request, "graphs/graphs.html", context)

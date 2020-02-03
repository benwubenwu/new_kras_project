from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
# AllProPhos, ColonTumorsPhos, PancreasTumorsPhos, WholePancreasPhos, ScrapedColonPhos
from .models import PancreasTumorPro, ScrapedColonPro, WholePancreasPro, ColonTumorPro, AllProteins
from plotly.offline import plot
import plotly.graph_objects as go
from django.http import HttpRequest
from django.db.models import Q
# Create your views here.


def about(request):
    return render(request, 'graphs/about.html')


def contact(request):
    return render(request, 'graphs/contact.html')


def search(request):
    return render(request, "graphs/search.html")


def search_results(request):

    query = request.GET.get('user_input')

    if query and request.method == 'GET':
        all_pro = AllProteins.objects.filter(
            Q(protein_id__icontains=query) | Q(
                gene_symbol__icontains=query) | Q(description__icontains=query))
        context = {
            'all_pro': all_pro
        }
    else:
        all_pro = AllProteins.objects.all()
        context = {
            'all_pro': all_pro
        }

    return render(request, "graphs/search_results.html", context)


def graphs(request, id):
    # protein/gene info
    all_pro = AllProteins.objects.get(id=id)
    gene_symbol = all_pro.gene_symbol
    description = all_pro.description
    protein_id = all_pro.protein_id

    try:
        pancreas_tumor_pro = PancreasTumorPro.objects.get(id=id)
        pancreas_tumor_pro_pdx_1 = pancreas_tumor_pro.wt_1
        pancreas_tumor_pro_pdx_2 = pancreas_tumor_pro.wt_2
        pancreas_tumor_pro_pdx_3 = pancreas_tumor_pro.wt_3
        pancreas_tumor_pro_pdxp53_1 = pancreas_tumor_pro.wt_4
        pancreas_tumor_pro_pdxp53_2 = pancreas_tumor_pro.wt_5
        pancreas_tumor_pro_pdxp53_3 = pancreas_tumor_pro.wt_6
        pancreas_tumor_pro_d314 = pancreas_tumor_pro.g12d_1
        pancreas_tumor_pro_d693 = pancreas_tumor_pro.g12d_2
        pancreas_tumor_pro_d705 = pancreas_tumor_pro.g12d_3
        pancreas_tumor_pro_d751 = pancreas_tumor_pro.g12d_4
        pancreas_tumor_pro_d756 = pancreas_tumor_pro.g12d_5
        pancreas_tumor_pro_average_norm_wt = pancreas_tumor_pro.average_norm_wt
        pancreas_tumor_pro_average_norm_g12d = pancreas_tumor_pro.average_norm_g12d
        pancreas_tumor_pro_average_norm_g12d_average_norm_wt = pancreas_tumor_pro.ratio_norm_g12d_norm_wt
        pancreas_tumor_pro_p_value = pancreas_tumor_pro.p_value
        pancreas_tumor_pro_boot_ratio = pancreas_tumor_pro.boot_ratio
        pancreas_tumor_pro_lower_ci = pancreas_tumor_pro.lower_ci
        pancreas_tumor_pro_upper_ci = pancreas_tumor_pro.upper_ci
        pancreas_tumor_pro_log_ratio = pancreas_tumor_pro.log_ratio
        pancreas_tumor_pro_log_lower_ci_diff = pancreas_tumor_pro.log_lower_ci_diff
        pancreas_tumor_pro_log_upper_ci_diff = pancreas_tumor_pro.log_upper_ci_diff

    except PancreasTumorPro.DoesNotExist:
        pancreas_tumor_pro = None

    try:
        scraped_colon_pro = ScrapedColonPro.objects.get(id=id)
        scraped_colon_pro_fabp_1 = scraped_colon_pro.norm_wt_1
        scraped_colon_pro_fabp_2 = scraped_colon_pro.norm_wt_2
        scraped_colon_pro_fabp_4 = scraped_colon_pro.norm_wt_3
        scraped_colon_pro_fabp_5 = scraped_colon_pro.norm_wt_4
        scraped_colon_pro_g12d_1 = scraped_colon_pro.norm_g12d_1
        scraped_colon_pro_g12d_2 = scraped_colon_pro.norm_g12d_2
        scraped_colon_pro_g12d_3 = scraped_colon_pro.norm_g12d_3
        scraped_colon_pro_g12d_4 = scraped_colon_pro.norm_g12d_4
        scraped_colon_pro_average_norm_wt = scraped_colon_pro.average_norm_wt
        scraped_colon_pro_average_norm_g12d = scraped_colon_pro.average_norm_g12d
        scraped_colon_pro_average_norm_g12d_average_norm_wt = scraped_colon_pro.ratio_norm_g12d_norm_wt
        scraped_colon_pro_p_value = scraped_colon_pro.p_value
        scraped_colon_pro_boot_ratio = scraped_colon_pro.boot_ratio
        scraped_colon_pro_lower_ci = scraped_colon_pro.lower_ci
        scraped_colon_pro_upper_ci = scraped_colon_pro.upper_ci
        scraped_colon_pro_log_ratio = scraped_colon_pro.log_ratio
        scraped_colon_pro_log_lower_ci_diff = scraped_colon_pro.log_lower_ci_diff
        scraped_colon_pro_log_upper_ci_diff = scraped_colon_pro.log_upper_ci_diff

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
        whole_pancreas_pro_average_norm_g12d_average_norm_wt = whole_pancreas_pro.ratio_norm_g12d_norm_wt
        whole_pancreas_pro_p_value = whole_pancreas_pro.p_value
        whole_pancreas_pro_boot_ratio = whole_pancreas_pro.boot_ratio
        whole_pancreas_pro_lower_ci = whole_pancreas_pro.lower_ci
        whole_pancreas_pro_upper_ci = whole_pancreas_pro.upper_ci
        whole_pancreas_pro_log_ratio = whole_pancreas_pro.log_ratio
        whole_pancreas_pro_log_lower_ci_diff = whole_pancreas_pro.log_lower_ci_diff
        whole_pancreas_pro_log_upper_ci_diff = whole_pancreas_pro.log_upper_ci_diff
    except WholePancreasPro.DoesNotExist:
        whole_pancreas_pro = None

    try:
        colon_tumor_pro = ColonTumorPro.objects.get(id=id)
        colon_tumor_pro_control1 = colon_tumor_pro.wt_1
        colon_tumor_pro_control2 = colon_tumor_pro.wt_2
        colon_tumor_pro_control3 = colon_tumor_pro.wt_3
        colon_tumor_pro_control4 = colon_tumor_pro.wt_4
        colon_tumor_pro_control5 = colon_tumor_pro.wt_5
        colon_tumor_pro_kras1 = colon_tumor_pro.g12d_1
        colon_tumor_pro_kras2 = colon_tumor_pro.g12d_2
        colon_tumor_pro_kras3 = colon_tumor_pro.g12d_3
        colon_tumor_pro_kras4 = colon_tumor_pro.g12d_4
        colon_tumor_pro_kras5 = colon_tumor_pro.g12d_5
        colon_tumor_pro_average_norm_wt = colon_tumor_pro.average_norm_wt
        colon_tumor_pro_average_norm_g12d = colon_tumor_pro.average_norm_g12d
        colon_tumor_pro_average_norm_g12d_average_norm_wt = colon_tumor_pro.ratio_norm_g12d_norm_wt
        colon_tumor_pro_p_value = colon_tumor_pro.p_value
        colon_tumor_pro_boot_ratio = colon_tumor_pro.boot_ratio
        colon_tumor_pro_lower_ci = colon_tumor_pro.lower_ci
        colon_tumor_pro_upper_ci = colon_tumor_pro.upper_ci
        colon_tumor_pro_log_ratio = colon_tumor_pro.log_ratio
        colon_tumor_pro_log_lower_ci_diff = colon_tumor_pro.log_lower_ci_diff
        colon_tumor_pro_log_upper_ci_diff = colon_tumor_pro.log_upper_ci_diff

    except ColonTumorPro.DoesNotExist:
        colon_tumor_pro = None

    # try:
    #     colon_tumor_phos = ColonTumorsPhos.objects.filter(id=id)
    # except ColonTumorsPhos.DoesNotExist:
    #     colon_tumor_phos = None

    # try:
    #     scraped_colon_phos = ScrapedColonPhos.objects.filter(id=id)
    # except ScrapedColonPhos.DoesNotExist:
    #     scraped_colon_phos = None

    # try:
    #     pancreas_tumor_phos = PancreasTumorsPhos.objects.filter(id=id)
    # except PancreasTumorsPhos.DoesNotExist:
    #     pancreas_tumor_phos = None

    # try:
    #     whole_pancreas_phos = WholePancreasPhos.objects.filter(id=id)
    # except WholePancreasPhos.DoesNotExist:
    #     whole_pancreas_phos = None

    def box_ce():
        layout = dict(
            title="",
            template="plotly_white",
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        # scraped colon protein
        try:
            scp_wt = [scraped_colon_pro_fabp_1, scraped_colon_pro_fabp_2,
                      scraped_colon_pro_fabp_4, scraped_colon_pro_fabp_5]
            scp_g12d = [scraped_colon_pro_g12d_1, scraped_colon_pro_g12d_2,
                        scraped_colon_pro_g12d_3, scraped_colon_pro_g12d_4]
            fig.add_trace(go.Box(x=['WT', 'WT', 'WT', 'WT'], y=scp_wt, name='WT',
                                 marker_color='#636EFA', boxpoints='all', pointpos=0))
            fig.add_trace(go.Box(x=['G12D', 'G12D', 'G12D', 'G12D'], y=scp_g12d, name='G12D',
                                 marker_color='#636EFA', boxpoints='all', pointpos=0))
        except:
            fig.add_trace(go.Box(y=[], name='Colonic epithelium WT'))
            fig.add_trace(go.Box(y=[], name='Colonic epithelium G12D'))
        fig.update_layout(
            xaxis={'title': 'Colonic epithelium'},
            yaxis={'title': None}
        )
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def box_ct():

        layout = dict(
            title="",
            template="plotly_white",
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        # colon tumor protein
        try:
            ctp_wt = [colon_tumor_pro_control1, colon_tumor_pro_control2,
                      colon_tumor_pro_control3, colon_tumor_pro_control4, colon_tumor_pro_control5]
            ctp_g12d = [colon_tumor_pro_kras1, colon_tumor_pro_kras2,
                        colon_tumor_pro_kras3, colon_tumor_pro_kras4, colon_tumor_pro_kras5]
            fig.add_trace(go.Box(x=['WT', 'WT', 'WT', 'WT', 'WT'], y=ctp_wt, name='WT',
                                 marker_color='indianred', boxpoints='all', pointpos=0))
            fig.add_trace(go.Box(x=['G12D', 'G12D', 'G12D', 'G12D', 'G12D'], y=ctp_g12d, name='G12D',
                                 marker_color='indianred', boxpoints='all', pointpos=0))
        except:
            fig.add_trace(go.Box(y=[], name='Apc-mutant colon WT'))
            fig.add_trace(go.Box(y=[], name='Apc-mutant colon G12D'))
        fig.update_layout(
            xaxis={'title': 'Apc-mutant colon'},
            yaxis={'title': None}
        )  
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)      
        return plot_div

    def box_wp():
        layout = dict(
            title="",
            template="plotly_white",
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        # whole pancreas protein
        try:
            wpp_wt = [whole_pancreas_pro_wt_1, whole_pancreas_pro_wt_2,
                      whole_pancreas_pro_wt_3, whole_pancreas_pro_wt_4]
            wpp_g12d = [whole_pancreas_pro_g12d_1,
                        whole_pancreas_pro_g12d_2, whole_pancreas_pro_g12d_3]
            fig.add_trace(go.Box(x=['WT', 'WT', 'WT', 'WT'], y=wpp_wt, name='WT',
                                 marker_color='lightseagreen', boxpoints='all', pointpos=0))
            fig.add_trace(go.Box(x=['G12D', 'G12D', 'G12D'], y=wpp_g12d, name='G12D',
                                 marker_color='lightseagreen', boxpoints='all', pointpos=0))
        except:
            fig.add_trace(go.Box(y=[], name='Whole pancreas WT'))
            fig.add_trace(go.Box(y=[], name='Whole pancreas G12D'))
        fig.update_layout(
            xaxis={'title': 'Whole pancreas'},
            yaxis={'title': None}
        )              
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)  
        return plot_div

    def box_pt():

        layout = dict(
            title="",
            template="plotly_white",
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        # pancreas tumor protein
        try:
            ptp_wt = [pancreas_tumor_pro_pdx_1,
                      pancreas_tumor_pro_pdx_2, pancreas_tumor_pro_pdx_3,
                      pancreas_tumor_pro_pdxp53_1, pancreas_tumor_pro_pdxp53_2,
                      pancreas_tumor_pro_pdxp53_3]
            ptp_g12d = [pancreas_tumor_pro_d314, pancreas_tumor_pro_d693,
                        pancreas_tumor_pro_d705, pancreas_tumor_pro_d751, pancreas_tumor_pro_d756]
            fig.add_trace(go.Box(x=['WT', 'WT', 'WT', 'WT', 'WT', 'WT'], y=ptp_wt, name='WT',
                                 marker_color='rgb(102,102,102)', boxpoints='all', pointpos=0))
            fig.add_trace(go.Box(x=['G12D', 'G12D', 'G12D', 'G12D', 'G12D'], y=ptp_g12d, name='G12D',
                                 marker_color='rgb(102,102,102)', boxpoints='all', pointpos=0))
        except:
            fig.add_trace(go.Box(y=[], name='Tp53-mutant pancreas WT'))
            fig.add_trace(go.Box(y=[], name='Tp53-mutant pancreas G12D'))
        fig.update_layout(
            xaxis={'title': 'Tp53-mutant pancreas'},
            yaxis={'title': None}
        )   
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)             
        return plot_div

    def scatter():
        layout = dict(
            template="plotly_white",
            # paper_bgcolor="rgba(0,0,0,0)",
            # plot_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=False, zeroline=True,
                       showline=True,categoryarray=['Tp53-mutant pancreas','Whole pancreas','Apc-mutant colon','Colonic epithelium'],categoryorder="array"),
            xaxis=dict(showgrid=False, showline=True, rangemode='tozero'),
            showlegend=False
        )
        fig = go.Figure(layout=layout)
        try:
            ptp_ratio = pancreas_tumor_pro_log_ratio
            ptp_lower = pancreas_tumor_pro_log_lower_ci_diff
            ptp_upper = pancreas_tumor_pro_log_upper_ci_diff
            fig.add_trace(go.Scatter(
                x=[ptp_ratio], y=['Tp53-mutant pancreas'], error_x=dict(type='data', symmetric=False, array=[ptp_upper], arrayminus=[ptp_lower]), mode="markers", marker_color='rgb(102,102,102)', marker=dict(size=[10])))
        except:
            test = 0
        try:
            ctp_ratio = colon_tumor_pro_log_ratio
            ctp_lower = colon_tumor_pro_log_lower_ci_diff
            ctp_upper = colon_tumor_pro_log_upper_ci_diff
            fig.add_trace(go.Scatter(
                x=[ctp_ratio], y=['Apc-mutant colon'], error_x=dict(type='data', symmetric=False, array=[ctp_upper], arrayminus=[ctp_lower]), mode="markers", marker_color='indianred', marker=dict(size=[10])))
        except:
            test = 0
        try:
            scp_ratio = scraped_colon_pro_log_ratio
            scp_lower = scraped_colon_pro_log_lower_ci_diff
            scp_upper = scraped_colon_pro_log_upper_ci_diff
            fig.add_trace(go.Scatter(
                x=[scp_ratio], y=['Colonic epithelium'], error_x=dict(type='data', symmetric=False, array=[scp_upper], arrayminus=[scp_lower]), mode="markers", marker_color='#636EFA', marker=dict(size=[10])))
        except:
            test = 0
        try:
            wpp_ratio = whole_pancreas_pro_log_ratio
            wpp_lower = whole_pancreas_pro_log_lower_ci_diff
            wpp_upper = whole_pancreas_pro_log_upper_ci_diff
            fig.add_trace(go.Scatter(
                x=[wpp_ratio], y=['Whole pancreas'], error_x=dict(type='data', symmetric=False, array=[wpp_upper], arrayminus=[wpp_lower]), mode="markers", marker_color='lightseagreen', marker=dict(size=[10])))
        except:
            test = 0
        # fig.add_shape(go.layout.Shape(type="line", x0=1, x1=1,
        #                               y0=-1, y1=3.1, line=dict(color="#5bc0de", width=1.5, dash='dot')))
        # fig.update_shapes(dict(xref='x'))
        # fig.update_layout(xaxis_type="log")
        fig.update_layout(
            xaxis={'title': 'Ratio of levels in G12D to WT (log-scaled)'},
            yaxis={'title': None}
        )
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'box_ce': box_ce(),
        'box_ct': box_ct(),
        'box_wp': box_wp(),
        'box_pt': box_pt(),
        'gene_symbol': gene_symbol,
        'all_pro': all_pro,
        'scatter': scatter(),
        'scp': scraped_colon_pro,
        'ctp': colon_tumor_pro,
        'ptp': pancreas_tumor_pro,
        'wpp': whole_pancreas_pro
        # 'scp_pvalue':scraped_colon_pro_p_value,
        # 'ctp_pvalue':colon_tumor_pro_p_value,
        # 'ptp_pvalue':pancreas_tumor_pro_p_value,
        # 'wpp_pvalue':whole_pancreas_pro_p_value
        # 'colon_tumor_phos': colon_tumor_phos,
        # 'scraped_colon_phos': scraped_colon_phos,
        # 'whole_pancreas_phos': whole_pancreas_phos,
        # 'pancreas_tumor_phos': pancreas_tumor_phos

    }
    return render(request, "graphs/graphs.html", context)

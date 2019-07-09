from django.shortcuts import render
import plotly
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from django.db.models import Q
from .models import dummy_for_histo_and_cloud, TimeGraph, histo_2
import random
import math
from django.http import HttpResponse

# 히스토그램 뽑아내기 위한 전역변수들
list_x = []
list_y = []
list_test = []
max5_x_list = []
max5_y_list = []
ordinary_dict = {}


# 워드클라우드 뽑아내기 위한 전역변수들
freq = []
qu = ""

# 시계열데이터 뽑아내기 위한 전역변수들
times = []
keyword5 = []
amount = []
time_list = []

# 상대빈도수
com_list = []
r_x = []
r_y = []



class Graph_1(TemplateView):
    template_name = 'graph_1.html'
 
    # 히스토 그램 뽑아내기
    def get_context_data(self, **kwargs):
        global max5_x_list
        global max5_y_list

        context = super(Graph_1, self).get_context_data(**kwargs)

        data = [go.Bar(x=[max5_x_list[0], max5_x_list[1], max5_x_list[2], max5_x_list[3], max5_x_list[4]], y=[max5_y_list[0], max5_y_list[1], max5_y_list[2], max5_y_list[3], max5_y_list[4]])]
        
        layout=go.Layout(title="핵심 빈출 키워드 분석 결과", xaxis={'title':'키워드'}, yaxis={'title':'빈도'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['Graph_1'] = div

        max5_x_list = []
        max5_y_list = []

        return context

# 워드클라우드 표현 샘플
# 현재 들어가 있는 데이터는 DB에서 받아오지 않은 일반 더미 데이터
class Graph_2(TemplateView):
    template_name = 'graph_2.html'

    def get_context_data(self, **kwargs):
        global list_x
        global list_y
        global freq

        freq = list(list_test.values_list('y_axis_quantity', flat=True))

        context = super(Graph_2, self).get_context_data(**kwargs)

        # words = ['5G', '빅데이터', '부정채용', '채용비리', '이석채', '올레TV', '김성태', 'SK telecom', '기가지니', 'IPTV',
        #         'KT아현지사', '기업전용5G', '슈퍼플랜', '황창규', '안전통신망', 'KT요금제', 'KT로밍', '아현화재', 'CCTV', 'KT고객센터']
        
        # frequency = [3400, 2950, 2200, 2050, 1500, 1200, 1000, 780, 750, 730,
        #             700, 680, 650, 630, 615, 600, 550, 540, 535, 520]

        # 워드클라우드 키워드와 빈도수 생성
        words = list_x
        frequency = freq

        weights=[]
        for i in frequency:
            weights.append(i//10)

        colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]

        data = go.Scatter(
            x=[random.random() for i in range(30)],
            y=[random.random() for i in range(30)],
            mode='text',
            text=words,
            marker={'opacity': 0.3},
            textfont={'size': weights,
            'color': colors}
            )
            
        layout = go.Layout(
            {'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
            'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
            'title' : '워드 클라우드',
            
            }
            
            )
        
        figure = go.Figure(data=[data], layout=layout)
        
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['Graph_2'] = div

        return context

class Graph_3(TemplateView):
    template_name = 'graph_3.html'

    def get_context_data(self, **kwargs):

        context = super(Graph_3, self).get_context_data(**kwargs)

        # 임의의 더미데이터 넣어준 상태
        # x는 기간을 의미
        # y는 해당 기간에 특정 키워드의 빈도수

        # global keyword5
        # global amount
        # global times
        global time_list
        #print(time_list)

        # 이런식으로 이터레이션 돌린다.
        # times = []
        # keyword5 = []
        # amount5 = []

        final = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []


        for elem in time_list:
            final.append(time_return(elem.time))
            final.append(elem.x_axis_keyword)
            final.append(elem.y_axis_quantity)
        
        #print(final)
        
        list1 = final[:18]
        #print(list1)
        list2 = final[18:36]
        #print(list2)
        list3 = final[36:54]
        list4 = final[54:72]
        list5 = final[72:90]
        

        #print(final)
        # print(times)
        # print(keyword5)
        # print(amount5)

        

        # 1~6 까지 상하반기 3번이 반복된다.
        x1 = [1, 2, 3, 4, 5, 6]
        y1 = [list1[2], list1[5], list1[8], list1[11], list1[14], list1[17]]

        x2 = [1, 2, 3, 4, 5, 6]
        y2 = [list2[2], list2[5], list2[8], list2[11], list2[14], list2[17]]

        x3 = [1, 2, 3, 4, 5, 6]
        y3 = [list3[2], list3[5], list3[8], list3[11], list3[14], list3[17]]

        x4 = [1, 2, 3, 4, 5, 6]
        y4 = [list4[2], list4[5], list4[8], list4[11], list4[14], list4[17]]

        x5 = [1, 2, 3, 4, 5, 6]
        y5 = [list5[2], list5[5], list5[8], list5[11], list5[14], list5[17]]

        # trace 를 정의해줌으로써 위 x와 y데이터를 꺾은선 그래프로 표현
        trace1 = go.Scatter(
            x = x1,
            y = y1,
            name = list1[1]
        )

        trace2 = go.Scatter(
            x = x2,
            y = y2,
            name = list2[1]
        )

        trace3 = go.Scatter(
            x = x3,
            y = y3,
            name = list3[1]
        )

        trace4 = go.Scatter(
            x = x4,
            y = y4,
            name = list4[1]
        )

        trace5 = go.Scatter(
            x = x5,
            y = y5,
            name = list5[1]
        )

        # plotly에게 실제로 우리가 해당 trace들을 쓰겠다고 지정해주는 부분

        data = [trace1, trace2, trace3, trace4, trace5]

        layout = go.Layout(
            title="시계열 데이터 분석 결과",
            xaxis = go.layout.XAxis(
                tickmode = 'array',
                # tickvals는 기간으로 설정해준 데이터를 의미하고 --> 사실 정확히 왜 필요한지 아직 깨닫지 못한 상태 by 현우(2019.05.09)
                # ticktext는 해당 기간들을 각각 어떤 식으로 naming 할 것인지 설정
                tickvals = [1, 2, 3, 4, 5, 6],
                ticktext = ['2018 1월-3월', '2018 4월-6월', '2018 7월-9월', '2018 10월-12월',
                            '2019 1월-3월', '2019 4월-6월']
                            
            )
        )
        
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        
        context['Graph_3'] = div

        return context

class Graph_4(TemplateView):
    template_name = 'graph_4.html'
 
    # 히스토 그램 뽑아내기
    def get_context_data(self, **kwargs):
        global r_x
        r_x = list(com_list.values_list('x_axis_keyword', flat=True))

        global r_y
        r_y = list(com_list.values_list('y_axis_quantity', flat=True))

        context = super(Graph_4, self).get_context_data(**kwargs)

        data = [go.Bar(x=[r_x[0], r_x[1], r_x[2], r_x[3], r_x[4], r_x[5], r_x[6], r_x[7], r_x[8], r_x[9]], y=[r_y[0], r_y[1], r_y[2], r_y[3], r_y[4], r_y[5], r_y[6], r_y[7], r_y[8], r_y[9]])]
        
        layout=go.Layout(title="유의미한 키워드", xaxis={'title':'키워드'}, yaxis={'title':'점수'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['Graph_4'] = div

        return context

def home(request):
    return render(request, 'home.html')

# 분석 결과 보여주는 페이지-----------------------------
def result(request):
    query = request.GET.get('q')
    show_name = " "

    # 쿼리 이름 다른거 예외처리
    list_1 =['LG CNS', 'LG cns', 'lg cns', '엘지 씨엔에스', 'CNS', 'cns', '씨엔에스']
    if(query in list_1):
        query = "1"
        show_name = "LG CNS"

    list_2 =['네이버', 'naver', 'Naver', 'NAVER']
    if(query in list_2):
        query = "2"
        show_name = "네이버"

    list_3 =['SDS', 'sds', '삼성 sds', '삼성 SDS', '삼성 에스디에스']
    if(query in list_3):
        query = "3"
        show_name = "삼성 SDS"

    list_4 =['쿠팡', 'coupang', 'Counpang',]
    if(query in list_4):
        query = "4"
        show_name = "쿠팡"

    list_5 =['구글', '구글코리아', '구글 코리아', 'google', 'GOOGLE']
    if(query in list_5):
        query = "5"
        show_name = "구글 코리아"

    list_6 =['카카오', 'KAKAO', 'kakao']
    if(query in list_6):
        query = "6"
        show_name = "카카오"

    list_7 =['배민', '배달의민족', '배달의 민족']
    if(query in list_7):
        query = "7"
        show_name = "배달의 민족"

    list_8 =['AWS', 'aws', 'Aws', '아마존 웹 서비스']
    if(query in list_8):
        query = "8"
        show_name = "AWS"

    list_9 =['C&C', 'sk C&C', 'SK C&C', '씨엔씨', 'SK 씨엔씨']
    if(query in list_9):
        query = "9"
        show_name = "SK C&C"

    list_10 =['퀄컴']
    if(query in list_10):
        query = "10"
        show_name = "퀄컴"

    global list_test
    list_test = dummy_for_histo_and_cloud.objects.filter(company_name=query)

    # 시계열 데이터 처리
    global time_list
    time_list = TimeGraph.objects.filter(company_name=query)

    #히스토그램2
    global com_list
    com_list = histo_2.objects.filter(company_name=query)
    #print(com_list)

    # global keyword5
    # keyword5 = list(time_list.values_list('x_axis_keyword', flat=True))
    # #print(keyword5)
    # global amount
    # amount = list(time_list.values_list('y_axis_quantity', flat=True))
    # #print(amount)
    # global times
    # times = list(time_list.values_list('time', flat=True))
    #print(times)



    
    
    global qu
    qu = list_test

    global list_x
    global list_y

    list_x = list(list_test.values_list('x_axis_keyword', flat=True))
    list_y = list(list_test.values_list('y_axis_quantity', flat=True))


    global ordinary_dict

    ordinary_dict = dict(zip(list_x, list_y))

    global max5_x_list
    global max5_y_list

    for i in range(0, 5, 1):
        max_v = max(list_y)
        max5_y_list.append(max_v)
        list_y.remove(max_v)

    for elem in max5_y_list:
        for name, age in ordinary_dict.items():
            if elem == age:
                max5_x_list.append(name)
    
    #print(max5_x_list)

    #key_list= dummy_for_histo_and_cloud.objects.filter(x_axis_keyword="홀리몰리")
    
    all_list = []

    for elem in max5_x_list:
        a = dummy_for_histo_and_cloud.objects.filter(x_axis_keyword=elem).filter(company_name=query)
        #print(a)
        for elem in a:
            all_list.append(elem.related_keyword_1)
            all_list.append(elem.related_keyword_2)
            all_list.append(elem.related_keyword_3)
            all_list.append(elem.related_keyword_4)
            all_list.append(elem.related_keyword_5)
    
    #print(all_list)

    a = all_list[:5]
    b = all_list[5:10]
    c = all_list[10:15]
    d = all_list[15:20]
    e = all_list[20:25]

    f_list = []

    for i in range(0, 5, 1):
        f_list.append(a[i])
        f_list.append(b[i])
        f_list.append(c[i])
        f_list.append(d[i])
        f_list.append(e[i])
    
    #print(f_list)

    a = f_list[:5]
    b = f_list[5:10]
    c = f_list[10:15]
    d = f_list[15:20]
    e = f_list[20:25]

    global r_x

    context = {
        'name' : show_name,
        'keyword_5' : max5_x_list,
        'a' : a,
        'b' : b,
        'c' : c,
        'd' : d,
        'e' : e,
        'r_x' : r_x,
    }
    return render(request, 'result.html', context)

def graph_1(request):
    graph = Graph_1()
    context =  graph.get_context_data()
    return render(request, 'graph_1.html', context)

def graph_2(request):
    graph = Graph_2()
    context =  graph.get_context_data()
    return render(request, 'graph_2.html', context)

def graph_3(request):
    graph = Graph_3()
    context =  graph.get_context_data()   
    return render(request, 'graph_3.html', context)

def graph_4(request):
    graph = Graph_4()
    context =  graph.get_context_data()   
    return render(request, 'graph_4.html', context)

def time_return(num):
    if num == "1":
        return '2017 상반기'
    elif num == "2":
        return '2017 하반기'
    elif num == "3":
        return '2018 상반기'
    elif num == "4":
        return '2018 하반기'
    elif num == "5":
        return '2019 상반기'
    elif num == "6":
        return '2019 하반기'
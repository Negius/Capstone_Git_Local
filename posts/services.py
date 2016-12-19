# this is file to store all common code 
from posts.models import  PostAccepted, LiveNews, Post, PostAccept, PostRate, PostType, PostSubType , Infor


# get LIVE NEWS FLAG
def get_live_news_flag():
    list_obj = LiveNews.objects.all()
    for obj in list_obj:
        if obj.was_commit_recently() == True:   #only get JUST COMMIT LIVE NEWS (< 2h)
            return  True
    return False
# get LIVE NEWS   
def get_live_news(flag_live_news):
    list_live_news = []
    if flag_live_news == True:
        list_object = LiveNews.objects.all()
        for obj in list_object:
            if obj.was_commit_recently() == True:
                dict_live_news = {}
                dict_live_news["content"] = obj.pub_time.strftime("%d/%m/%Y-%H:%M") + " Round: " + str(obj.round) + " " + obj.host.name + " " + str(obj.host_point) + " - " + str(obj.quest_point) + " " + obj.quest.name
                dict_live_news["id"] = obj.pk
                list_live_news.append(dict_live_news)
    else :
        list_object = PostAccepted.objects.order_by('commit_date')[0:3]
        for obj in list_object:
            dict_live_news = {}
            dict_live_news["content"] = obj.commit_date.strftime("%d/%m/%Y") + " " + obj.title
            dict_live_news["id"] = obj.pk
            list_live_news.append(dict_live_news) 
    return list_live_news
# get HOT NEWS
def get_hot_news():
    list_hot_news = PostAccepted.objects.filter(is_hot=True).order_by('commit_date')[0:3]
    return list_hot_news
#get Page INFO
def get_page_infor():
    list_page_infor = Infor.objects.all()
    return list_page_infor[0]
# get PAGE INFOR +  LIVE NEWS
def get_base_list():
    context = {}
    page_infor = get_page_infor()
    context['page_infor'] = page_infor
    list_live_news_flag = get_live_news_flag()
    list_live_news = get_live_news(get_live_news_flag())
    if list_live_news_flag:
        context['list_live_news_flag'] = list_live_news_flag
        context['list_live_news'] = list_live_news
    else :
        context['list_live_news'] = list_live_news
    return context
    
#get type and subtype ==> set toolbar 

#get TOP 5 
def get_top_five():
    type_news = PostSubType.objects.filter(name="News")
    type_video = PostSubType.objects.filter(name="Video")
    type_gallery = PostSubType.objects.filter(name="Gallery")
    type_guide = PostSubType.objects.filter(name="Guide")
    
    print (type_news)
    print (type_gallery)
    print (type_video)
    print (type_guide)
    return type_news
        
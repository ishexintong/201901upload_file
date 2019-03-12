from django.shortcuts import render,HttpResponse

import uuid
import os
import json
# Create your views here.
def index(request):
    '''
    upload the file
    :param request:
    :return:
    '''
    if request.method=='GET':

        return render(request,'index.html')

    username=request.POST.get('username')
    avatar=request.FILES.get('custom_excel')
    with open(avatar.name,'wb') as f:
        for line in avatar.chunks():
            f.write(line)
    return HttpResponse('ok')

def form_data_upload(request):
    '''
    预处理图像的上传
    :param request:
    :return:
    '''
    if request.method=='POST':
        img_obj=request.FILES.get('img_upload')
        filename= str(uuid.uuid4())+'.'+img_obj.name.rsplit('.',maxsplit=1)[1]
        img_file_path=os.path.join('static','imgs',filename)
        with open(img_file_path,'wb') as f:
            for line in img_obj.chunks():
                f.write(line)
        return HttpResponse(img_file_path)
def upload_img(request):
    '''
    upload the image
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'up3.html')
    return HttpResponse('upload the image success.')

def upload_iframe(request):
    '''
    处理iframe 上传图片，返回图片的路径
    :param request:
    :return:
    '''
    ret={'status':True,'data':None}
    try:
        img_obj=request.FILES.get('avatar')
        filename = str(uuid.uuid4()) + '.' + img_obj.name.rsplit('.', maxsplit=1)[1]
        img_file_path = os.path.join('static', 'imgs', filename)
        with open(img_file_path, 'wb') as f:
            for line in img_obj.chunks():
                f.write(line)
        ret['data']=img_file_path
    except Exception as e:
        ret['status']=False
        ret['error']='上传失败'
    return HttpResponse(json.dumps(ret))
def iframe_upload_img(request):
    '''
    处理iframe upload img 的请求
    :param request:
    :return:
    '''

    return render(request,'iframe_upload_img.html')
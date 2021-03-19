from django.shortcuts import render,redirect
import africastalking
from home.models import*

import codecs
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import urllib,json

import datetime
from random import randint
from django.core.signing import Signer
from django.views.decorators.csrf import csrf_exempt
username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"


@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_numer = request.POST.get('phonenumer')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        num = text[:3]

        if text == '':
            response = 'CON murakaza neza kurubuga rwabahinzi Smart ikigega \n'
            response += '1.ikigega pay \n'
            response += '2.ibijyanye numusaruro \n'
            response += '3.kwiyandikisha mukigega \n'
            response += '4.kubarura umusaruro \n'
            #  harvesting session
        elif text == '1':
            response = 'CON kwishyura \n'
            response += '1.uri mukigega \n'
            response += '2.momo isanzwe'
        elif text == '1*1':
            response = 'CON shyiramo code yumuhinzi '+str(level)+' \n' 
            # if Farmers.objetcs.filter(code=str(level[2])).exists():
            #     response = 'CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
            # else:
            #     response = 'END code washyizemo ntibaho '+str(level)+' \n'
   
        elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON shyiramo amafaranga ugiye kwishyura \n' 
        elif num == '1*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
            insert=Harvestrecord(code=str(level[2]),Quantity=str(level[3]))
            insert.save()
        elif text == '1*2':
            response = 'CON nimero ya mobile : '+str(len(level))+ '\n'        
            # insert=Harvestrecord.objects.create(farmercode=str(level[2]))
            # insert.save()
        # elif num == '1*2' and int(len(level))==2 and str(level[3]) in str(level):
        #     response = 'CON umubare wamafaranga  \n'
        # elif num == '1*2' and int(len(level))==3 and str(level[4]) in str(level):
        #     response = 'CON wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'   
         
        
        # elif text == '2':
        #     response = 'CON  hitamo \n'
        #     response += '1.kureba umusaruro mbumbe \n'
        #     response += '2.ubwishingizi bwumusaruro \n'
        #     response += '3.ikigega Loan'
        # elif text == '2*1':
        #     response = 'CON  shyiramo code yawe ubashe kureba umusaruro :' +str(len(level))+ '\n'
            
        # elif num == '2*1'and int(len(level))==3 and str(level[2]) in str(level):
        #     # insert=Harvestrecord(Quantity=str(level[3]))
        #     # if insert.is_valid():
        #      response = 'CON hitamo kureba \n'
        #      response += '1.umusaruro wukukwezi\n'
        #      response += '2.umusaruro mbumbe wose'
        #     # response = 'CON code mwashyizemo ntibaho : \n'
                 
        # elif text =='2*1*1':
        #     response = 'CON umusaruro wa' + str(level[2]) +'wukukwezi ni 360kg'+str(level[3])+'\n'
        # elif text =='2*1*2':
        #     response = 'CON umusaruro mbumbe wa' + str(level[2]) + 'ni 3600kg'+str(level[3])+'\n'
        # elif text == '2*2':
        #     response = 'CON  ubwishingizi bw \n'
        #     response += '1.umwaka umwe \n'
        #     response += '2.imyaka itanu  \n'
        #     response += '3.imyaka icumi '   
        # elif text == '2*2*1':
        #     response = 'CON  shyiramo code yawe ubashe kwinjira mu bwishingizi bwumwaka umwe:' +str(len(level))+ '\n'
        # elif num == '2*2*1'and int(len(level))==4 and str(level[3]) in str(level):
        #      response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'   
        #     #  insert=Insurance.objects.filter(farmercode=str(level[4])) 
        #     #  insert.save()     

        # elif text == '2*2*2':
        #     response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
        # elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):  
        #     response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n' 
        #     # insert=Insurance.objects.filter(farmercode=str(level[4])) 
        #     # insert.save()                        
        #     # response = 'CON code mwashyizemo ntibaho : \n'
        # elif text == '3':
        #     response = 'CON  hitamo kwiyandikisha  nk \n'
        #     response += '1. itsinda(cooperative)\n'
        #     response += '2.umuhinzi ku giti cye '
        # elif text == '3*1':
        #     response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
        #     # insert = Cooperativesreg.objects.create(name=str(level[2]))
        #     # insert.save() 
        # elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
        #     response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
        #     # insert= Cooperativesreg.objects.create(leadername=str(level[3]))
        #     # insert.save()   

        # elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
        #     # insert= Cooperativesreg.objects.create(leaderphone=str(level[4]))
        #     # insert.save()   
        # elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
        #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
        # elif text == '3*2':
        #     response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
        #     # insert= Regfarmer.objects.create(firstname=str(level[2]))
        #     # insert.save()
        # elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
        #     response = 'CON  shyiramo izina rya kabiri \n'
        #     # insert= Regfarmer.objects.create(lastname=str(level[3]))
        #     # insert.save()
        # elif num == '3*2'and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON  shyiramo numero yawe ya telephone \n'
        #     # insert= Regfarmer.objects(telephone=str(level[4]))    
        #     # insert.save()

        # elif num == '3*2' and int(len(level))==5 and str(level[4]) in str(level):  
        #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
        # elif text == '4':
        #     response = 'CON  shyiramo code yawe ubashe kubarura :' +str(len(level))+ '\n'
        # elif num == '4'and int(len(level))==2 and str(level[1]) in str(level):  
        #     response = 'CON  shyiramo izina rya cooperative \n'  
        #     # insert=Cooperative.objects.filter(name=str(level[2]))  
        #     # insert.save()
        # elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
        #     response = 'CON  shyiramo code yumuhinzi \n'  
        #     # insert=Harvestrecord.objects.filter(farmercode=str(level[3]))  
        #     # insert.save()
        # elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
        #     response = 'CON  shyiramo ibiro yagize \n'  
        #     # insert=Harvestrecord.objects(Quantity=str(level[4]))  
        #     # insert.save()    
        else:
            response = 'END Invalid Choice'
        
        return HttpResponse(response)

    return HttpResponse('harvest')    

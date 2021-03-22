from django.shortcuts import render,redirect
import africastalking
from .models import*

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
username = "tuganimana01@gmail.com"
api_key = "d06d5d1c7bf8213c4f354f39cc114aef2d03faef644f17b11cc9142a256758bf"
africastalking.initialize(username, api_key)

@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':

        # session_id = request.POST.get('sessionId')
        # service_code = request.POST.get('serviceCode')
        # phone_number = request.POST.get("phoneNumber")
        session_id = request.values.get("sessionId", None)
        service_code = request.values.get("serviceCode", None)
        phone_number = request.values.get("phoneNumber", None)
        text = request.values.get("text", "default")

        level = text.split('*')
        response = ''
        num = text[:3]
        # farmers=Farmers.objects.all().filter(number=phone_number).order_by('-id')
        # for users in farmers:
        #     phoneuser = users.number
        #     fullname = users.fullname
        #     mypin = users.pincode
        # if farmers.exists():
            
        if text == '':
            response = "CON Murakaza neza kurubuga rw'abahinzi Smart Ikigega \n"
            response += '1.Ikigega pay \n'
            response += '2.ibijyanye numusaruro \n'
            response += '3.kwiyandikisha muri COOPERATIVE \n'
            response += '4.kubarura umusaruro \n'
                #  harvesting session
        # elif text == '1':
        #     response = 'CON kwishyura \n'
        #     response += '1.uri mukigega \n'
        #     response += '2.momo isanzwe'
        # elif text == '1*1':
        #     response = 'CON shyiramo code yumuhinzi '+str(level)+' \n' 
        #     if Farmers.objetcs.filter(code=str(level[2])).exists():
        #         response = 'CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
        #     else:
        #         response = 'END code washyizemo ntibaho '+str(level)+' \n'
    
        # elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON shyiramo amafaranga ugiye kwishyura \n' 
        # elif num == '1*1' and int(len(level))==5 and str(level[4]) in str(level):
        #     response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
        #     insert=Harvestrecord(code=str(level[2]),Quantity=str(level[3]))
        #     insert.save()
        # elif text == '1*2':
        #     response = 'CON nimero ya mobile : '+str(len(level))+ '\n'
        #     insert=Harvestrecord.objects.create(farmercode=str(level[2]))
        #     insert.save()
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
        #         # insert=Harvestrecord(Quantity=str(level[3]))
        #         # if insert.is_valid():
        #     response = 'CON hitamo kureba \n'
        #     response += '1.umusaruro wukukwezi\n'
        #     response += '2.umusaruro mbumbe wose'
        #         # response = 'CON code mwashyizemo ntibaho : \n'
                    
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
        #     response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'   
        #         #  insert=Insurance.objects.filter(farmercode=str(level[4])) 
        #         #  insert.save()     

        # elif text == '2*2*2':
        #     response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
        # elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):  
        #     response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n' 
        #         # insert=Insurance.objects.filter(farmercode=str(level[4])) 
        #         # insert.save()                        
        #         # response = 'CON code mwashyizemo ntibaho : \n'
        # elif text == '3':
        #     response = 'CON  hitamo kwiyandikisha  nk \n'
        #     response += '1. itsinda(cooperative)\n'
        #     response += '2.umuhinzi ku giti cye '
        # elif text == '3*1':
        #     response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
        #         # insert = Cooperativesreg.objects.create(name=str(level[2]))
        #         # insert.save() 
        # elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
        #     response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
        #         # insert= Cooperativesreg.objects.create(leadername=str(level[3]))
        #         # insert.save()   

        # elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
        #         # insert= Cooperativesreg.objects.create(leaderphone=str(level[4]))
        #         # insert.save()   
        # elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
        #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
        # elif text == '3*2':
        #     response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
        #         # insert= Regfarmer.objects.create(firstname=str(level[2]))
        #         # insert.save()
        # elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
        #     response = 'CON  shyiramo izina rya kabiri \n'
        #         # insert= Regfarmer.objects.create(lastname=str(level[3]))
        #         # insert.save()
        # elif num == '3*2'and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON  shyiramo numero yawe ya telephone \n'
        #         # insert= Regfarmer.objects(telephone=str(level[4]))    
        #         # insert.save()

        # elif num == '3*2' and int(len(level))==5 and str(level[4]) in str(level):  
        #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
        # elif text == '4':
        #     response = 'CON  shyiramo code yawe ubashe kubarura :' +str(len(level))+ '\n'
        # elif num == '4'and int(len(level))==2 and str(level[1]) in str(level):  
        #     response = 'CON  shyiramo izina rya cooperative \n'  
        #         # insert=Cooperative.objects.filter(name=str(level[2]))  
        #         # insert.save()
        # elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
        #     response = 'CON  shyiramo code yumuhinzi \n'  
        #         # insert=Harvestrecord.objects.filter(farmercode=str(level[3]))  
        #         # insert.save()
        # elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
        #     response = 'CON  shyiramo ibiro yagize \n'  
        #         # insert=Harvestrecord.objects(Quantity=str(level[4]))  
        #         # insert.save()    
        else:
            response = 'END Invalid Choice'
    return HttpResponse(response)
            # farmers=Farmers.objects.all().filter(number=phone_number).order_by('-id')
            # for users in farmers:
            #     phoneuser = users.number
            #     fullname = users.fullname
            #     mypin = users.pincode
            # if farmers.exists():
                
                
                
        # else:

            
        #     if text=='':
        #         response = "CON Ikaze kuri Smart Kigega, Iyandikishe mu kigega \n"
        #         response +="1.Iyandikishe \n"     
        #     elif text =='1':
        #         response = "CON Andika amazina yawe \n"

        #     elif int(st)==1  and int(len(level))==2  and   str(level[1]) in str(level):
        #        response = "CON Shyiramo Umubare w'ibanga wawe \n"
        #     elif int(st)==1  and int(len(level))==3  and   str(level[2]) in str(level):
        #        response = "CON Andika akarere utuyemo \n" 
        #     elif int(st)==1  and int(len(level))==4  and   str(level[3]) in str(level):
        #         response = "CON Andika Umurenge utuyemo \n"
        #     elif int(st)==1  and int(len(level))==5  and   str(level[4]) in str(level):
        #         pin=str(level[2])
        #         district =str(level[3])
        #         sector =str(level[4])
        #         pincode = make_password(pin)
        #         def random_with_N_digits(n):
        #             range_start = 10**(n-1)
        #             range_end = (10**n)-1
        #             return randint(range_start, range_end)
        #             numb = random_with_N_digits(5)
        #             insert =Farmers(number=phone_number,code=numb,sector=sector,district=district, fullname=str(level[1]),pincode=pin,joined_on=created_on)
        #             try:
                    
        #                 insert.save()
        #                 telephone = phone_number[1:]
        #                 response = "END Urakoze kwiyandikisha kuri Smart Kigega,Numero y'ibanga yanyu ni: "+str(pin)+". \n Kubindi bisobanuro sura https://www.smartkigega.com"
                        
        #             except:
        #                 response = "END Kwiyandikisha byanze"
        #     else:

        #             response = "END Invalid choice"    

    return HttpResponse('harvest-ussd app-smart ikigega')    
  
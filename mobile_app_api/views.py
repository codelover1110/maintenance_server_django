from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, ShopData, AdminUser, VoteData, MetaData, DegreeDay, Consumption
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
# Create your views here.
def getUser(request, email, password):
    try:
        user = get_object_or_404(User, email = email)
        if user.password == password:
            data = {
                'email': user.email,
                'password': user.password
            }
        else:
            data = {
                'email': user.email,
                'password': ''
            }
    except:
        data = {
                'email': '',
                'password': ''
            }
    return  JsonResponse(data)

def getAdminUser(request):
    userInfor = json.loads(request.body.decode('utf-8'))
    username = userInfor['username']
    print(username)
    user = AdminUser.objects.filter(user_name = username)
    if user:
      try:
          user = get_object_or_404(AdminUser, user_name = username)
          if  user.password == userInfor['password']:
              data = {
                'user_name': user.user_name,
                'password': user.password
              }
          else:
            data = {
              'user_name': user.user_name,
              'password': ''
            }
      except:
        data = {
          'user_name': '',
          'password': ''
        }
    else:
      data = {
        'user_name': '',
        'password': ''
      }

    return  JsonResponse(data)

def getAdminUsers(request):
  users = AdminUser.objects.all()
  user_list = []
  for user in users:
    item = model_to_dict(user)
    user_list.append(item)

  return JsonResponse(user_list, safe=False)

def getCustomerUsers(request):
  users = VoteData.objects.all()
  user_list = []
  for user in users:
    item = model_to_dict(user)
    user_list.append(item)

  return JsonResponse(user_list, safe=False)

def addUser(request):
    try:
        User.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['password'],
            age = request.POST['age'],
            gender = request.POST['gender'],
        )
        data = {"success": "true" }
    except:
        data = {"success": "false"}

    return JsonResponse(data)

def addAdminUser(request):
    if request.method == "POST":
        details = json.loads(request.body.decode('utf-8'))
    try:
        AdminUser.objects.create(
            email = details['email'],
            password = details['password'],
            user_name = details['username']
        )
        data = {"success": "true" }
    except:
        data = {"success": "false" }


    return JsonResponse(data)

def manageShopData(request):
    print(request.FILES['cover'])
    content = json.loads(request.POST.get('content'))
    print(content['nfcID'])
    try:
      ShopData.objects.create(
          store_picture = request.FILES['cover'],
          nfc_uid = content['nfcID'],
          nfc_store_id = content['nfcStoreID'],
          store_name = content['storeName'],
          store_address = content['storeAddress'],
          store_postcode = content['storePostcode'],
          stroe_city = content['storeCity'],
          longtitude = content['longtitude'],
          latitude = content['latitude']
      )
      data = {"success": "true" }
    except:
      data = {"success": "false"}
   
    return JsonResponse(data)

def home(request): 
    return HttpResponse('Hello, ShopVote!')
    
def deleteAdminUser(request, id):
  print(id)
  user = AdminUser.objects.get(id = id)
  if user:
    user.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})  

def deleteCustomerUser(request, id):
  print(id)
  user = VoteData.objects.get(id = id)
  if user:
    user.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})

def getShopDatas(request):
  shopDatas = ShopData.objects.all()
  shop_list = []
  for shopData in shopDatas:
    item = model_to_dict(shopData)
    if (item.get('store_picture')):
        item['store_picture'] = str(item.get('store_picture'))
        print(item)

    shop_list.append(item)

  return JsonResponse(shop_list, safe=False)

def getShopData(request, id):
  shopdata = model_to_dict(ShopData.objects.get(id = id))
  shopdata['store_picture'] = str(shopdata.get('store_picture'))
  return JsonResponse(shopdata)

def updateShopData(request, id):
  try:
    content = json.loads(request.POST.get('content'))
    shopData = ShopData.objects.get(id=id)
    
    shopData.nfc_uid = content['nfcID']
    shopData.nfc_store_id = content['nfcStoreID']
    shopData.store_name = content['storeName']
    shopData.store_address = content['storeAddress']
    shopData.store_postcode = content['storePostcode']
    shopData.stroe_city = content['storeCity']
    shopData.longtitude = content['longtitude']
    shopData.latitude = content['latitude']
    shopData.save()
    shopData.store_picture.save(str(shopData.store_picture), request.FILES['cover'])

    
    data = {"success": "false"}
  except:
    data = {"success": "true"}


  return JsonResponse(data)

def deleteShopData(request, id):
  print(id)
  shopData = ShopData.objects.get(id = id)
  if shopData:
    shopData.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})

def getCustomerShopData(request, shopid):
  shopdata = model_to_dict(ShopData.objects.get(nfc_store_id = shopid))
  shopdata['store_picture'] = str(shopdata.get('store_picture'))
  return JsonResponse(shopdata)


def manageVoteData(request):
    content = request.POST
    # try:
    VoteData.objects.create(
        customer_email = content['cutomerID'],
        vote_name = 'Service',
        vote = content['serviceStatus'],
        nfc_store_id = content['nfc_store_id'],
        shop_name = content['shopName'],
        longtitude = content['longtitude'],
        latitude = content['latitude'],
    )
    VoteData.objects.create(
        customer_email = content['cutomerID'],
        vote_name = 'Tilgængelighed',
        vote = content['availabilityStatus'],
        shop_name = content['shopName'],
        nfc_store_id = content['nfc_store_id'],
        longtitude = content['longtitude'],
        latitude = content['latitude'],
    )
    VoteData.objects.create(
        customer_email = content['cutomerID'],
        vote_name = 'Udvalg',
        vote = content['selectionStatus'],
        nfc_store_id = content['nfc_store_id'],
        shop_name = content['shopName'],
        longtitude = content['longtitude'],
        latitude = content['latitude'],
    )
    data = {"success": "true" }
    # except:
    #   data = {"success": "false"}
   
    print(data)
    return JsonResponse(data)


# CRUD metadata
def createMetaData(request):
    print(request.FILES['cover'])
    content = json.loads(request.POST.get('content'))
    try:
      MetaData.objects.create(
          meta_data_picture = request.FILES['cover'],
          tag_id = content['tagID'],
          nfc_tag = content['nfcTag'],
          media_type = content['mediaType'],
          energy_media_type = content['energyMediaType'],
          meter_point_description = content['meterPointDescription'],
          energy_unit = content['energyUnit'],
          group = content['group'],
          column_line = content['columnLine'],
          meter_location = content['meterLocation'],
          energy_art = content['energyArt'],
          supply_area_child = content['supplyAreaChild'],
          meter_level_structure = content['meterLevelStructure'],
          supply_area_parent = content['supplyAreaParent'],
          longtitude = content['longtitude'],
          latitude = content['latitude']
      )
      data = {"success": "true" }
    except:
      data = {"success": "false"}
   
    return JsonResponse(data)

def getMetadatas(request):
  metaDatas = MetaData.objects.all()
  data_list = []
  for metaData in metaDatas:
    item = model_to_dict(metaData)
    if (item.get('meta_data_picture')):
        item['meta_data_picture'] = str(item.get('meta_data_picture'))
        print(item)

    data_list.append(item)

  return JsonResponse(data_list, safe=False)

def getMetaData(request, id):
  metadata = model_to_dict(MetaData.objects.get(id = id))
  metadata['meta_data_picture'] = str(metadata.get('meta_data_picture'))
  return JsonResponse(metadata)

def updateMetaData(request, id):
  try:
    content = json.loads(request.POST.get('content'))
    metaData = MetaData.objects.get(id=id)
    
    metaData.tag_id = content['tagID']
    metaData.nfc_tag = content['nfcTag']
    metaData.media_type = content['mediaType']
    metaData.energy_media_type = content['energyMediaType']
    metaData.meter_point_description = content['meterPointDescription']
    metaData.energy_unit = content['energyUnit']
    metaData.group = content['group']
    metaData.column_line = content['columnLine']
    metaData.meter_location = content['meterLocation']
    metaData.energy_art = content['energyArt']
    metaData.supply_area_child = content['supplyAreaChild']
    metaData.meter_level_structure = content['meterLevelStructure']
    metaData.supply_area_parent = content['supplyAreaParent']
    metaData.supply_area_parent = content['supplyAreaParent']
    metaData.longtitude = content['longtitude']
    metaData.latitude = content['latitude']
    metaData.save()
    metaData.meta_data_picture.save(str(metaData.meta_data_picture), request.FILES['cover'])

    
    data = {"success": "false"}
  except:
    data = {"success": "true"}


  return JsonResponse(data)

def deleteMetaData(request, id):
  print(id)
  metaData = MetaData.objects.get(id = id)
  if metaData:
    metaData.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})


# CRUD DegreeDays
def createDegreeDay(request):
    content = json.loads(request.POST.get('content'))
    try:
      DegreeDay.objects.create(
          name_of_degree = content['name_of_degree'],
          period_form = content['period_form'],
          period_to = content['period_to'],
          month = content['month'],
          degree_days = content['degree_days'],
          
      )
      data = {"success": "true" }
    except:
      data = {"success": "false"}
   
    return JsonResponse(data)

def getDegreeDays(request):
  degreeDays = DegreeDay.objects.all()
  data_list = []
  for degreeDay in degreeDays:
    item = model_to_dict(degreeDay)
    data_list.append(item)

  return JsonResponse(data_list, safe=False)

def editDegreeDay(request, id):
  degreeDay = model_to_dict(DegreeDay.objects.get(id = id))
  return JsonResponse(degreeDay)

def updateDegreeDay(request, id):
  try:
    content = json.loads(request.POST.get('content'))
    degreeDay = DegreeDay.objects.get(id=id)
    
    degreeDay.name_of_degree = content['name_of_degree']
    degreeDay.period_form = content['period_form']
    degreeDay.period_to = content['period_to']
    degreeDay.month = content['month']
    degreeDay.degree_days = content['degree_days']
   
    degreeDay.save()

    
    data = {"success": "false"}
  except:
    data = {"success": "true"}


  return JsonResponse(data)

def deleteDegreeDay(request, id):
  degreeDay = DegreeDay.objects.get(id = id)
  if degreeDay:
    degreeDay.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})



# CRUD DegreeDays
def createConsumption(request):
    content = json.loads(request.POST.get('content'))
    try:
      Consumption.objects.create(
          tag_id = content['tag_id'],
          nfc_tag = content['nfc_tag'],
          date = content['date'],
          consumption = content['consumption'],
          unit = content['unit'],
          
      )
      data = {"success": "true" }
    except:
      data = {"success": "false"}
   
    return JsonResponse(data)

def getConsumptions(request):
  consumptions = Consumption.objects.all()
  data_list = []
  for consumption in consumptions:
    item = model_to_dict(consumption)
    data_list.append(item)

  return JsonResponse(data_list, safe=False)

def editConsumption(request, id):
  consumption = model_to_dict(Consumption.objects.get(id = id))
  return JsonResponse(consumption)

def updateConsumption(request, id):
  try:
    content = json.loads(request.POST.get('content'))
    consumption = Consumption.objects.get(id=id)
    
    consumption.tag_id = content['tag_id']
    consumption.nfc_tag = content['nfc_tag']
    consumption.date = content['date']
    consumption.consumption = content['consumption']
    consumption.unit = content['unit']
   
    consumption.save()

    
    data = {"success": "false"}
  except:
    data = {"success": "true"}


  return JsonResponse(data)

def deleteConsumption(request, id):
  consumption = Consumption.objects.get(id = id)
  if consumption:
    consumption.delete()
    return JsonResponse({'success': 'true'})
  else:
    return JsonResponse({'success': 'false'})




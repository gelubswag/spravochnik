from django.shortcuts import render,redirect
from .models import Name, Fam, Otc, Street, MainItem, Phones
from .forms import NameForm, FamForm, OtcForm, StreetForm, MainItemForm
# Create your views here.

def get_filtered_Maindata(request, data):
            if request.POST.get('tel') and 'tel' in data.keys():
                tel = request.POST.get('tel')
                del data['tel']
        
            else:
                tel = None
            MainItems = [i.load_phones() for i in MainItem.objects.filter(**data).all()]
            filtered_data = []
            if tel:
                for item in MainItems:
                    phones_list = [str(i) for i in item.tel]
                    if tel in phones_list:
                            print(type(tel))
                            filtered_data.append(item)
                MainItems = filtered_data
            else:
                filtered_data = MainItems
            return MainItems   

def get_filtered_Maindata_ADD(request, data):
            if request.POST.get('tel'):
                tel = request.POST.get('tel')
            else:
                tel = None
            MainItems = MainItem.objects.filter(**data).all()
            return MainItems   
        
def change_fk(request, ParentTable, ItemPK):
    match ParentTable:
        case 'Name':
            model = Name
            form = NameForm
        case 'Fam':
            model = Fam
            form = FamForm
        case 'Otc':
            model = Otc
            form = OtcForm
        case 'Street':
            model = Street
            form = StreetForm
        case _:
            return redirect('spravApp:main')
    context = {
            'pageTitle': f'Change {ParentTable}',
            'form': form(instance=model.objects.filter(id=ItemPK).all()[0]),
        }
    if request.method == 'GET':
        return render(request, 'form.html', context)
    else:
        data = {}
        if request.POST.get('id'): data['id'] = request.POST.get('id')
        if request.POST.get('val'): data['val'] = request.POST.get('val')
        try:
            item = model.objects.filter(id=ItemPK).update(**data)
            return redirect('spravApp:ParentTable', ParentTable=ParentTable)
        except Exception as ex:
            context['error'] = f'Ошибка при изменении: {ex}'
            return render(request, 'form.html', context)
    
def get_post_data(request):
        data = {}
        if request.POST.get('id'): data['id'] = request.POST.get('id')
        if request.POST.get('fam'): data['fam'] = request.POST.get('fam')
        if request.POST.get('name'): data['name'] = request.POST.get('name')
        if request.POST.get('otc'): data['otc'] = request.POST.get('otc')
        if request.POST.get('street'): data['street'] = request.POST.get('street')
        if request.POST.get('bldn'): data['bldn'] = request.POST.get('bldn')
        if request.POST.get('bldn_k'): data['bldn_k'] = request.POST.get('bldn_k')
        if request.POST.get('appr'): data['appr'] = request.POST.get('appr')
        if request.POST.get('tel'): data['tel'] = request.POST.get('tel')
        # if request.POST.get('val'): data['tel'] = request.POST.get('val')
        return data

def get_foreign_key_data(request):
        data = get_post_data(request)
        if request.POST.get('fam'): data['fam'] = Fam.objects.filter(id=request.POST.get('fam')).all()[0]
        if request.POST.get('name'): data['name'] = Name.objects.filter(id=request.POST.get('name')).all()[0]
        if request.POST.get('otc'): data['otc'] = Otc.objects.filter(id=request.POST.get('otc')).all()[0]
        if request.POST.get('street'): data['street'] = Street.objects.filter(id=request.POST.get('street')).all()[0]
        
        return data   
       
def mainItemChange(request, ItemPK):
    context = {
            'pageTitle': 'MainItemChange',
            'MainItems': MainItem.objects.filter(id=ItemPK).all(),
            'form': MainItemForm(instance=MainItem.objects.filter(id=ItemPK).all()[0]),
        }
    if request.method == 'GET':
        
        return render(request, 'form.html', context)
    else:
        data = get_foreign_key_data(request)
        try:
            item = MainItem.objects.filter(id=ItemPK).update(**data)
            return redirect('spravApp:main')
        except Exception as ex:
            context['error'] = f'Ошибка при изменении: {ex}'
            return render(request, 'form.html', context)
      
        
        

def main(request):
    if request.method == 'GET':
        MainItems = [i.load_phones() for i in MainItem.objects.all()]
        context = {
            'pageTitle': 'Main',
            'MainItems': MainItems,
            'form': MainItemForm(),
        }
        return render(request, 'main.html', context)
    else:
        data = get_post_data(request)
        if "search" in request.POST:
            MainItems = get_filtered_Maindata(request, data)
                            
            context = {
            'pageTitle': 'Main',
            'MainItems': MainItems,
            'form': MainItemForm(),
            }
            return render(request, 'main.html', context)
        
        elif "add" in request.POST:
            data = get_foreign_key_data(request)
            MainItems = get_filtered_Maindata(request, data)
            print(MainItems)

                        
            if MainItems:
                context = {
                'pageTitle': 'Main',
                'MainItems': MainItem.objects.filter(**data).all(),
                'form': MainItemForm(),
                }
                context['error'] = 'Контакт с заданнымы параметрами уже существует'
                return render(request, 'main.html', context)
            else:
                if request.POST.get('tel'): 
                    tel = request.POST.get('tel')
                MainItems = get_filtered_Maindata(request, data)
                if not MainItems:
                    try:
                        item = MainItem.objects.create(**data)
                        item.save()
                        try:
                            Phones.objects.create(val=tel, person=item).save()
                        except:
                            Phones.objects.create(val='', person=item).save()
                        context = {
                            'pageTitle': 'Main',
                            'MainItems': [i.load_phones() for i in MainItem.objects.filter(**data).all()],
                            'form': MainItemForm(),
                            }
                        return render(request, 'main.html', context)
                    except Exception as ex:
                        context = {
                            'pageTitle': 'Main',
                            'MainItems': MainItems,
                            'form': MainItemForm(),
                            'error': f'Не удалось добавить контакт: {ex}'
                            }
                        return render(request, 'main.html', context)
                else:
                    for item in MainItems:
                        try:
                            Phones.objects.create(val=tel, person=item).save()
                        except:
                            Phones.objects.create(val='', person=item).save()
                        item.save()
                        context = {
                            'pageTitle': 'Main',
                            'MainItems': [i.load_phones() for i in MainItems],
                            'form': MainItemForm(),
                            }
                        return render(request, 'main.html', context)
        elif "change" in request.POST:
            data = get_foreign_key_data(request)
        
            
            MainItems = MainItem.objects.filter(**data).all()
            
            context = {
                'pageTitle': 'Main',
                'MainItems': MainItems,
                'form': MainItemForm(),
                }
            if len(MainItems) == 0:
                context['error'] = 'Контакт с заданными параметрами не найден'
                return render(request, 'main.html', context)
            elif len(MainItems) > 1:
                context['error'] = 'Найдено несколько контактов с заданными параметрами'
                return render(request, 'main.html', context)
            else:
                return redirect('spravApp:mainItemChange', ItemPK=MainItems[0].id)
    
        elif "delete" in request.POST:
            data = get_foreign_key_data(request)
            MainItems = MainItem.objects.filter(**data).all()
            context = {
                'pageTitle': 'Main',
                'MainItems': MainItems,
                'form': MainItemForm(),
                }
            if len(MainItems) == 0:
                context['error'] = 'Контакт с заданными параметрами не найден'
                return render(request, 'main.html', context)
            elif len(MainItems) > 1:
                context['error'] = 'Найдено несколько контактов с заданными параметрами'
                return render(request, 'main.html', context)
            else:
                MainItem.objects.filter(id=MainItems[0].id).delete()
                return redirect('spravApp:main')

def ParentTable(request,ParentTable):
    match ParentTable:
        case 'Name':
            model = Name
            form = NameForm
        case 'Fam':
            model = Fam
            form = FamForm
        case 'Otc':
            model = Otc
            form = OtcForm
        case 'Street':
            model = Street
            form = StreetForm
        case _:
            return redirect('spravApp:main')
    context = {
            'pageTitle': f'{ParentTable}',
            'Items': model.objects.all(),
            'form': form(),
            'field': ParentTable
        }
    if request.method == 'GET':
        return render(request, 'parentTable.html', context)
    else:
        data = {}
        if request.POST.get('id'): data['id'] = request.POST.get('id')
        if request.POST.get('val'): data['val'] = request.POST.get('val')
        if "search" in request.POST:
            Items = model.objects.filter(**data).all()
            
            context = {
            'pageTitle': f'{ParentTable}',
            'Items': Items,
            'form': form(),
            'field': ParentTable
            }
            return render(request, 'parentTable.html', context)
        
        elif "add" in request.POST:
            
            Items = model.objects.filter(**data).all()
            if Items:
                context = {
                'Items': Items,
                'form': form(),
                'field': ParentTable
                }
                context['error'] = 'Заданная строка уже существует'
                return render(request, 'parentTable.html', context)
            else:
                try:
                    model.objects.create(**data).save()
                
                    context = {
                        'Items': model.objects.filter(**data).all(),
                        'form': form(),
                        'field': ParentTable
                        }
                    return render(request, 'parentTable.html', context)
                except Exception as ex:
                    context = {
                        'Items': model.objects.filter(**data).all(),
                        'form': form(),
                        'error': f'Не удалось добавить в {ParentTable}: {ex}',
                        'field': ParentTable
                        }
                    return render(request, 'parentTable.html', context)
        
        elif "change" in request.POST:
            data = {}
            if request.POST.get('id'): data['id'] = request.POST.get('id')
            if request.POST.get('val'): data['val'] = request.POST.get('val')
            
            Items = model.objects.filter(**data).all()
            
            context = {
                'Items': Items,
                'form': form(),
                'field': ParentTable
                }
            if len(Items) == 0:
                context['error'] = 'Данная строка с заданными параметрами не найдена'
                return render(request, 'parentTable.html', context)
            elif len(Items) > 1:
                context['error'] = 'Найдено несколько строк с заданными параметрами'
                return render(request, 'parentTable.html', context)
            else:
                return redirect('spravApp:fk_change', ParentTable=ParentTable, ItemPK=Items[0].id)
    
        elif "delete" in request.POST:
            data = {}
            if request.POST.get('id'): data['id'] = request.POST.get('id')
            if request.POST.get('val'): data['val'] = request.POST.get('val')
            Items = model.objects.filter(**data).all()
            context = {
                'Items': Items,
                'form': form,
                'field': ParentTable
                }
            if len(Items) == 0:
                context['error'] = 'Контакт с заданными параметрами не найден'
                return render(request, 'parentTable.html', context)
            elif len(Items) > 1:
                context['error'] = 'Найдено несколько контактов с заданными параметрами'
                return render(request, 'parentTable.html', context)
            else:
                model.objects.filter(id=Items[0].id).delete()
                return redirect('spravApp:ParentTable', ParentTable=ParentTable)
        


# Create your views here.

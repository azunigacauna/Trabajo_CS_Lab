from django.shortcuts import render
# , get_object_or_404, redirect
# from .models import Profesion
# from .forms import AddForm

# # Create your views here.
# def index(request):
# 	profs = Profesion.objects.all()
# 	return render(request, "profesion.html", {'profs':profs})

# def profesionShowView(request, myID):
# 	obj = get_object_or_404( Profesion, ProCod= myID)
# 	context = {
# 		'objeto' : obj,
# 	}
# 	return render(request, 'profesion.html', context)

# def profesionCreateView(request):
# 	obj = Profesion.objects
# 	form = AddForm(request.POST or None)
	
# 	if form.is_valid():
# 		form.save()
# 		form = AddForm()
# 		return redirect('../')

# 	context = {
# 		'form': form,
# 	}
# 	return render(request, "profesionCreate.html", context)

# def profesionEditView(request, myID):
# 	obj = Profesion.objects.get(ProCod = myID)
# 	form = AddForm(request.POST or None, instance = obj)
	
# 	if form.is_valid():
# 		form.save()
# 		form = AddForm()
# 		return redirect('../../ListProfesion')

# 	context = {
# 		'form': form,
# 	}
# 	return render(request, "profesionEdit.html", context)

# def profesionDeleteView(request, myID):
# 	obj = get_object_or_404(Profesion, ProCod = myID)
# 	if request.method == 'POST':
# 		print("por fa imprime :0")
# 		obj.delete()
# 		return redirect('../../../ListProfesion')

# 	context = {
# 		'objeto': obj,
# 	}
# 	return render(request, "profesionDelete.html", context)

# def profesionListView(request):
# 	queryset = Profesion.objects.all()
# 	context = {
# 		'objectList': queryset,
# 	}
# 	return render(request, "profesionList.html", context)

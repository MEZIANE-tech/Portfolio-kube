from django.shortcuts import render
from Contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import FileResponse, Http404, HttpResponseRedirect, HttpResponse

# Create your views here.



MAX_MESSAGE_SIZE = 2
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Construire le contenu de l'email
            email_subject = f"Contact depuis le site : {subject}"
            email_body = (
                f"Nom : {first_name} {last_name}\n"
                f"Email : {email}\n\n"
                f"Message :\n{message}"
            )
            
            try:
                # Envoyer l'e-mail
                send_mail(
                    email_subject,
                    email_body,
                    'mezianeyacine14@gmail.com',  # Remplacez par votre adresse
                    ['mezianeyacine@outlook.fr'],  # Remplacez par l'adresse de réception
                )
                return render(request, 'contact/thank-you.html')
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'envoi de l'email : {e}")
        else:
            # Si le formulaire n'est pas valide, renvoyer le formulaire avec les erreurs
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})



def privacy_policy(request):
    return render(request, "contact/privacy-policy.html")
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

def send_mail(to, template, context):
	try:
		html_content = render_to_string(f'employee/emails/{template}.html', context)
		text_content = render_to_string(f'employee/emails/{template}.txt', context)

		msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
		msg.attach_alternative(html_content, 'text/html')
		msg.send()
	except:
		if settings.DEBUG:
			print("Error #23yrhjbewf5e3t : occured while sending mail")
		else:
			pass
	return


def send_activation_email(request, email, code):
	try:
		context = {
			'subject': _('Profile activation'),
			'uri': request.build_absolute_uri(reverse('employee:activate', kwargs={'code': code})),
		}

		send_mail(email, 'activate_profile', context)
	except:
		if settings.DEBUG:
			print("Error #463452daf : occured while sending mail")
		else:
			pass
	return

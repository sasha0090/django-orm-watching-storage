from datacenter.models import Passcard, Visit
from datacenter.models import format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    # Программируем здесь
    passcard_visits = Visit.objects.filter(passcard=passcard)
    
    
    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        duration = passcard_visit.get_duration()

        this_passcard_visits.append({
            "entered_at": passcard_visit.entered_at.strftime("%d-%m-%Y"),
            "duration": format_duration(duration),
            "is_strange": passcard_visit.is_long()
        })

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

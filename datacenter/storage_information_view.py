from datacenter.models import Passcard, Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []

    unfinished_visits = Visit.objects.filter(leaved_at=None)
    
    for unfinished_visit in unfinished_visits:
        passcard_owner = unfinished_visit.passcard.owner_name
        duration = unfinished_visit.get_duration()
        
        non_closed_visits.append({
            "who_entered": passcard_owner,
            "entered_at": unfinished_visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": unfinished_visit.is_long()
            })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


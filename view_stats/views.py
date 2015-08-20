from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Interval_Counters 

from . import timeintervals as ti
import datetime as dt

def all_stats(request):
    all_counters = Interval_Counters.objects.all()
    output = ' | '.join(["{0}:{1}".format(str(c.interval_key), str(c.count))
                            for c in all_counters])
    return HttpResponse(output + ' EOF')

def get_count(request, server, interval_start, interval_stop):
    count = ti.get_count(server, interval_start, interval_stop)
    return HttpResponse(str(count))

def get_IC_counts_in_range(request, r_server, r_interval, r_start, r_stop):
    r_start = long(r_start)
    r_stop = long(r_stop) + int(r_interval)
    counters_interval = Interval_Counters.objects.filter(
        server=r_server,
        interval_start__gte=r_start,
        interval_stop__lte=r_stop
    )
    output = ' | '.join(["{0}:{1}".format(str(c.interval_key), str(c.count))
                                            for c in counters_interval])
    return HttpResponse(output + ' EOF')

def get_counts_interval_range(request, server, interval, start, stop, unit_interval=20):
    interval = int(interval)    
    start = long(start)
    stop = long(stop)
    unit_interval = int(unit_interval)
    counts = ti.get_counts_interval_range(server, interval, start, stop, unit_interval)
    return HttpResponse(str(counts))

def get_union_counts_interval_range(request, interval, start, stop, unit_interval=20):
    interval = int(interval)    
    start = long(start)
    stop = long(stop)
    unit_interval = int(unit_interval)
    server = ['logstash', 'kafka']
    order, counts = ti.get_union_counts_interval_range(server, interval, start, stop, unit_interval)
    order = ['interval'] + order
    ordered_counts = [[ti.epoch_to_utc(i)] + counts[i] for i in sorted(counts, reverse=True)]
    
    counts = []
    for count_row in ordered_counts:
        matched = "synced"
        last_item = count_row[1]
        for item in count_row[1:]:
            if item != last_item:
                matched = "unsynced"
        counts += [{'matched': matched, 'data':count_row}]

    template = loader.get_template('view_stats/general_board.html')
    context = RequestContext(request, {
        'sources': order,
        'counts': counts,
    })
    return HttpResponse(template.render(context))

def general_union_view(request):
    return get_union_counts_interval_range_recent(request, 180, 20, 3600)

def get_union_counts_interval_range_recent(request, interval, unit_interval=20, rec_range=3600):
    interval = int(interval)
    stop = ti.bucket_datetime_epoch(interval, dt.datetime.utcnow())[1] - interval
    start = stop - rec_range
    ti.clean(rec_range)
    return get_union_counts_interval_range(request, interval, start, stop, unit_interval)

def post_counts(request, server, interval, start, stop, add_count):
    interval = int(interval)    
    start = long(start)
    stop = long(stop)
    i_c = ti.get_interval_counters(server, interval, start, stop)
    return HttpResponse(str(counts))

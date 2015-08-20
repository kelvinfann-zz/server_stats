from .models import Interval_Counters

import datetime
import time

EPOCH_ORIG=datetime.datetime(1970, 1, 1)

def get_inbetween_intervals(interval, start, stop):
    if (stop - start) % interval != 0:
        raise ValueError(("Bad arguments. Stop ({0}) - Start ({1}) % "
                          "Interval ({2}) != 0").format(stop, start, interval))
    inbetween_intervals = (stop - start) / interval
    return (start + (i * interval) for i in xrange(inbetween_intervals+1))

def get_intervals_in_range(server, start, stop):
    counters_interval = Interval_Counters.objects.filter(
        server=server,
        interval_start__gte=start,
        interval_stop__lte=stop,
    )
    return counters_interval

def get_interval_counters(server, interval_start, interval_stop):
    unique_interval_key = '{0}:{1}-{2}'.format(server, interval_start, interval_stop)
    interval_counter = Interval_Counters.objects.filter(
        server=server,
        interval_start=interval_start,
        interval_stop=interval_stop,
    )
    if interval_counter:
        interval_counter = interval_counter
    else:
        interval_counter = None
    return interval_counter

def get_count(server, interval_start, interval_stop):
    interval_counters =  get_interval_counters(server, interval_start, interval_stop)
    if interval_counters:
        count = sum(interval_counter.count for interval_counter in interval_counters)
    else:
        count = 0
    return count

def get_counts_interval_range(server, interval, start, stop, unit_interval):
    interval_iter = get_inbetween_intervals(interval, start, stop)
    counts = []
    for interval_step in interval_iter:
        counters = get_intervals_in_range(server, interval_step, interval_step + interval)
        count = sum(counter.count for counter in counters) + 0
        counts += [(interval_step, count)]
    return counts

def get_union_counts_interval_range(servers, interval, start, stop, unit_interval):
    base_range = get_counts_interval_range('', interval, start, stop, unit_interval)
    union_counts = {}
    order = []
    for i_s, count in base_range:
        union_counts[i_s] = []
    for server in servers:
        order += [server]
        counts = get_counts_interval_range(server, interval, start, stop, unit_interval)
        for i_s, count in counts:
            union_counts[i_s] += [count]
    return order, union_counts

def bucket_datetime_epoch(interval, dtime):
    """Returns the time interval (in seconds) that the dtime belongs to in epoch form

    Args:
        interval: the number of seconds (int) between each time interval. We 
        dtime: a datetime.time object that we are trying to get the bucket for

    Returns:
        An epoch representation of the timeinterval the dtime belongs to (in seconds)
        
    """

    bucket = bucket_time(interval, dtime)
    # bucket_hour, bucket_min, bucket_sec = sec_to_HMS(bucket)

    b_start = dtime.replace(hour=0, minute=0, second=0, microsecond=0)

    start_interval = long((b_start - EPOCH_ORIG).total_seconds()) + bucket
    end_interval = start_interval + interval

    return start_interval, end_interval

def bucket_time(interval, dtime):
    """Returns the time interval (in seconds) that the dtime belongs to

    Args:
        interval: the number of seconds (int) between each time interval. We 
        dtime: a datetime.time object that we are trying to get the bucket for

    Returns:
        An int representation of the timeinterval the dtime belongs to (in seconds)
        
    """

    sec_since_day = dtime.second + 60*(dtime.minute + 60*dtime.hour)
    return (sec_since_day / interval) * interval

def epoch_to_utc(epoch_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))

def clean(past_time=(60*60*24)):
    curr = bucket_datetime_epoch(1, datetime.datetime.utcnow())[0]
    to_delete_counters = Interval_Counters.objects.filter(
        interval_start__lte=curr-past_time,
    )
    for counter in to_delete_counters:
        counter.delete()
    return


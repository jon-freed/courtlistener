from django.core.exceptions import ValidationError
from django.utils.text import get_valid_filename


def make_upload_path(instance, filename):
    """Return a string like pdf/2010/08/13/foo_v._var.pdf"""
    try:
        # Cannot do proper type checking here because of circular import
        # problems when importing Audio, Document, etc.
        d = instance.file_with_date
    except AttributeError:
        raise NotImplementedError("This function cannot be used without a "
                                  "file_with_date attribute.")

    return '%s/%s/%02d/%02d/%s' % (
        filename.split('.')[-1],
        d.year,
        d.month,
        d.day,
        get_valid_filename(filename)
    )


def validate_partial_date(instance, field):
    """Ensure that partial dates make sense.

    Validates that:
     - Both granularity and date field are either completed or empty (one cannot
       be completed if the other is not).
     - If a partial date, the day/month is/are set to 01.
    """
    d = getattr(instance, 'date_%s' % field)
    granularity = getattr(instance, 'date_granularity_%s' % field)

    if any([d, granularity]) and not all([d, granularity]):
        raise ValidationError({
            'date_%s' % field: 'Date and granularity must both be complete or '
                               'blank.'
        })

    # If a partial date, are days/month set to 1?
    bad_date = False
    if granularity == instance.GRANULARITY_YEAR:
        if d.month != 1 and d.day != 1:
            bad_date = True
    if granularity == instance.GRANULARITY_MONTH:
        if d.day != 1:
            bad_date = True
    if bad_date:
        raise ValidationError({
            'date_%s' % field: 'Granularity was set as partial, but date '
                               'appears to include month/day other than 1.'
        })

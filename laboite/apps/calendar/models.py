# coding: utf-8
from datetime import datetime

from django.db import models
from django.utils import formats, timezone
from django.utils.translation import ugettext_lazy as _
from icalendar import Calendar
import pytz
import requests
import unidecode

from boites.models import App, HOURS


class AppCalendar(App):
    UPDATE_INTERVAL = 1 * HOURS

    ics_url = models.CharField(_('URL du calendrier .ics'),
                               help_text=_("Veuillez indiquer l'adresse de votre calendrier .ics"),
                               max_length=256,
                               default=None,
                               null=True)
    dtstart = models.CharField(_('Heure du prochain rendez-vous'), max_length=5, default=None, null=True)
    summary = models.CharField(_('Intitulé du prochain rendez-vous'), max_length=256, default=None, null=True)

    def update_data(self):
        # TODO: handle whole day events, display multiple events
        now = timezone.now()
        tonight = now.replace(hour=23, minute=59)

        self.dtstart = None
        self.summary = None

        calendar = Calendar()
        r = requests.get(self.ics_url)

        calendar = calendar.from_ical(r.text)

        for event in calendar.walk():
            if event.get('dtstart') and event.get('dtend'):
                dtstart = event.get('dtstart').dt
                dtend = event.get('dtend').dt
                if not isinstance(dtstart, datetime) or not isinstance(dtend, datetime):
                    dtstart = datetime.fromordinal(dtstart.toordinal())
                    dtend = datetime.fromordinal(dtend.toordinal())
                try:
                    dtstart = timezone.localtime(dtstart, timezone.utc)
                    dtend = timezone.localtime(dtend, timezone.utc)
                except ValueError:
                    dtstart = dtstart.replace(tzinfo=timezone.utc)
                    dtend = dtend.replace(tzinfo=timezone.utc)
                if now <= dtend <= tonight:
                    dtstart = timezone.localtime(dtstart, pytz.timezone('Europe/Paris'))
                    self.dtstart = formats.time_format(dtstart, 'TIME_FORMAT')
                    self.summary = str(unidecode.unidecode(event.get('summary')))
        self.save()

    def _get_data(self):
        if self.dtstart:
            return {
                'width': 32,
                'height': 16,
                'data': [
                    {
                        'type': 'bitmap',
                        'width': 8,
                        'height': 8,
                        'x': 0,
                        'y': 0,
                        'color': 1,
                        'content': '0xfefe8292929282fe'
                    },
                    {
                        'type': 'text',
                        'width': 25,
                        'height': 8,
                        'x': 7,
                        'y': 1,
                        'color': 2,
                        'font': 1,
                        'content': self.dtstart,
                    },
                    {
                        'type': 'text',
                        'width': 32,
                        'height': 8,
                        'x': 0,
                        'y': 9,
                        'color': 1,
                        'font': 1,
                        'content': self.summary,
                    }
                ]
            }
        else:
            return {
                'width': 32,
                'height': 16,
                'data': [
                    {
                        'type': 'bitmap',
                        'width': 8,
                        'height': 8,
                        'x': 12,
                        'y': 4,
                        'color': 2,
                        'content': '0xffff8185a99181ff'
                    },
                ]
            }

    class Meta:
        verbose_name = _('Configuration : calendrier')
        verbose_name_plural = _('Configurations : calendrier')

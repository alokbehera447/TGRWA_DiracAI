from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.db.models import Q
from account.models import Service


class Command(BaseCommand):
    help = "Populate empty or null slugs on Service and ensure uniqueness"

    def handle(self, *args, **options):
        qs = Service.objects.filter(Q(slug='') | Q(slug__isnull=True))
        total = qs.count()
        if total == 0:
            self.stdout.write(self.style.SUCCESS('No empty or null slugs found.'))
            return

        updated = 0
        for s in qs:
            base = slugify(getattr(s, 'title', '') or 'service')[:240]
            if not base:
                base = 'service'
            candidate = base
            i = 1
            while Service.objects.filter(slug=candidate).exclude(pk=s.pk).exists():
                candidate = f"{base[:235]}-{i}"
                i += 1
            s.slug = candidate
            s.save(update_fields=['slug'])
            updated += 1
            self.stdout.write(f"Updated Service id={s.pk} -> slug='{s.slug}'")

        self.stdout.write(self.style.SUCCESS(f'Finished: {updated} of {total} services updated.'))
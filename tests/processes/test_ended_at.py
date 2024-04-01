from django.utils import timezone
from model_bakery.baker import make

from processes.models import Process, ProcessStatus


def test_completed_status_sets_ended_at(db):
    process = make(Process, status=ProcessStatus.IN_PROGRESS)
    assert process.ended_at is None
    process.status = ProcessStatus.COMPLETED
    process.save()
    assert process.ended_at is not None


def test_change_status_from_completed_resets_ended_at(db):
    process = make(
        Process,
        status=ProcessStatus.COMPLETED,
        ended_at=timezone.now(),
    )
    assert process.ended_at is not None
    process.status = ProcessStatus.IN_PROGRESS
    process.save()
    assert process.ended_at is None

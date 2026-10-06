import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const requireCabinet = createRequire(new URL('../../../xuanxue-cabinet/package.json', import.meta.url));
const { DateTime } = requireCabinet('luxon');
function toIsoUtc(date) {
  const iso = DateTime.fromJSDate(date).toUTC().toISO();
  if (iso === null) throw new Error('invalid date');
  return iso;
}
// Exact projection body from Cabinet fc2dee2; only its TypeScript annotation is removed.
// Inputs are isolated lean-record fixtures. This is not an HTTP/database experiment.
function toPublicLessonDto(lesson, cls) {
  const dto = {
    id: lesson._id.toString(),
    classId: lesson.classId.toString(),
    startsAt: toIsoUtc(lesson.startsAt),
    durationMin: lesson.durationMin,
    classTitle: cls.title,
    groupLabel: cls.groupLabel,
    format: cls.format,
    topic: lesson.topic,
    status: lesson.status,
    // У дат до ADR-0075 поля `tags` в документе нет — контракт требует `[]`.
    tags: lesson.tags ?? [],
  };
  // Ключ `location` — только если адрес есть (контракт: «omitted when absent»).
  // Пустая строка — не «нет адреса»: контракт велит отдавать пустые строки как
  // есть, поэтому проверка на undefined, а не на truthy.
  if (cls.location !== undefined) dto.location = cls.location;
  return dto;
}

const id = { toString: () => '000000000000000000000003' };
const classId = { toString: () => '100000000000000000000001' };
const baseLesson = { _id: id, classId, startsAt: new Date('2026-10-06T15:00:00Z'), durationMin: 60, topic: '', status: 'scheduled', tags: [] };
const baseClass = { title: 'Test', groupLabel: '', format: 'both' };
const malformedLesson = { ...baseLesson };
delete malformedLesson.durationMin;
const omitted = JSON.parse(JSON.stringify(toPublicLessonDto(malformedLesson, baseClass)));
assert.equal(Object.hasOwn(omitted, 'durationMin'), false);
const malformedClass = JSON.parse(JSON.stringify(toPublicLessonDto(baseLesson, { ...baseClass, format: 'invalid-format' })));
assert.equal(malformedClass.format, 'invalid-format');
console.log(JSON.stringify({ sourceRevision: 'fc2dee20d64d91122a58e57709c378c5fc91bae7', scope: 'isolated mapper and JSON serialization', missingDurationOmitted: true, invalidClassEnumPassed: true }));

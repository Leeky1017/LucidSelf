export function getTimePositionPercent(time: string): number {
  const [hoursStr, minutesStr] = time.split(":");
  const hours = Number(hoursStr);
  const minutes = Number(minutesStr);

  if (!Number.isFinite(hours) || !Number.isFinite(minutes)) {
    return 50;
  }

  const totalMinutes = hours * 60 + minutes;
  const ratio = Math.min(Math.max(totalMinutes / (24 * 60), 0), 1);
  // Reverse: 24:00 at top (5%), 00:00 at bottom (95%)
  return 5 + (1 - ratio) * 90;
}

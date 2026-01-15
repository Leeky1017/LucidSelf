export type TimeScale = "hour" | "day" | "month" | "year";

export interface PersonalTimelineEntry {
  id: string;
  time: string;
  title: string;
  description: string;
  kind: "dream" | "reflection" | "event";
}

export interface LucidTimelineEntry {
  id: string;
  time: string;
  title: string;
  insight: string;
  confidence: number;
}

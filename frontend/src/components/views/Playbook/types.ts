export type TimeScope = "day" | "week" | "month" | "year";

export interface Engine {
  id: string;
  name: string;
  category: "eastern" | "western";
  enabled: boolean;
}

export interface SourceInfo {
  name: string;
  color: string;
  description: string;
  philosophy: string;
}

export interface InlineSource {
  start: number;
  end: number;
  sources: string[];
}

export interface ReadingParagraph {
  text: string;
  inlineSources: InlineSource[];
}

export interface DreamEntry {
  id: string;
  date: string;
  time: string;
  title: string;
  content: string;
  mood: string;
  symbols: string[];
  interpretation?: {
    summary: string;
    symbolMeanings: { symbol: string; meaning: string }[];
    connection: string;
  };
  realityConnection?: {
    date: string;
    event: string;
    correlation: string;
  };
}

export interface Topic {
  readonly id: number;
  readonly topicName: string;
}

export interface Card {
  readonly id: number;
  readonly topicId: number;
  readonly question: string;
  readonly answer: string;
}

export interface PractiseSession {
  readonly id: number;
  readonly topicId: number;
  readonly sessionStart: string;
}

export interface SessionCard {
  readonly id: number;
  readonly cardId: number;
  readonly userAnswer: string;
  readonly correct?: boolean;
}

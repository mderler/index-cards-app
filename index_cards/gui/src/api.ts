import { Card, PractiseSession, SessionCard, Topic } from "./models";
import csrftoken from "./token";

export class APIError extends Error {
  response: Response;

  constructor(response: Response) {
    super(response.statusText);
    this.response = response;
  }
}

export class APIInterface {
  static baseUrl = new URL("http://localhost:8000/api/");

  private static _modifyRequestOptions(requestOptions: RequestInit) {
    if (requestOptions.method === "GET") {
      requestOptions.mode = "cors";
      requestOptions.headers = {
        "Access-Control-Allow-Origin": window.location.origin,
      };
      return requestOptions;
    }
    if (
      requestOptions.method !== "POST" &&
      requestOptions.method !== "PUT" &&
      requestOptions.method !== "DELETE"
    ) {
      return requestOptions;
    }
    if (!csrftoken || !csrftoken.csrftoken) {
      throw new Error("CSRF Token undefined");
    }
    requestOptions.headers = {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken.csrftoken,
    };
    return requestOptions;
  }

  private static _fetchAPI(uri: string, requestOptions: RequestInit) {
    return fetch(
      new URL(uri, this.baseUrl),
      this._modifyRequestOptions(requestOptions)
    )
      .then((response) => {
        if (!response.ok) throw new APIError(response);
        return response;
      })
      .then((response) => {
        if (response.status === 204) {
          return;
        }
        return response.json();
      });
  }

  static async getTopics() {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI("topics/", requestOptions).then(
      (data) => data.data as Topic[]
    );
  }

  static async getTopic(id: number) {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions).then(
      (data) => data.data as Topic
    );
  }

  static async putTopic(id: number, topicName: string): Promise<Topic> {
    const requestOptions: RequestInit = {
      method: "PUT",
      body: JSON.stringify({ topicName: topicName }),
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions);
  }

  static async deleteTopic(id: number) {
    const requestOptions: RequestInit = {
      method: "DELETE",
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions);
  }

  static async postTopic(topicName: string): Promise<Topic> {
    const requestOptions: RequestInit = {
      method: "POST",
      body: JSON.stringify({ topicName: topicName }),
    };
    return await this._fetchAPI("topics/", requestOptions);
  }

  static async getCards() {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI("cards/", requestOptions).then(
      (data) => data.data as Card[]
    );
  }

  static async getTopicCards(topicId: number) {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI(`cards/${topicId}`, requestOptions).then(
      (data) => data.data as Card[]
    );
  }

  static async getCard(id: number) {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI(`card/${id}`, requestOptions).then(
      (data) => data.data as Card
    );
  }

  static async putCard(id: number, question?: string, answer?: string) {
    const requestOptions: RequestInit = {
      method: "PUT",
      body: JSON.stringify({ question: question, answer: answer }),
    };
    return (await this._fetchAPI(`card/${id}`, requestOptions)) as Card;
  }

  static async deleteCard(id: number) {
    const requestOptions: RequestInit = {
      method: "DELETE",
    };
    return await this._fetchAPI(`card/${id}`, requestOptions);
  }

  static async postCard(topicId: number) {
    const requestOptions: RequestInit = {
      method: "POST",
      body: JSON.stringify({ topicId: topicId }),
    };
    return await this._fetchAPI("cards/", requestOptions);
  }

  static async getPractiseSession(practiseSessionId: number) {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI(
      `practisesession/${practiseSessionId}`,
      requestOptions
    ).then((data) => data.data as PractiseSession);
  }

  static async getPractiseSessions() {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI("practisesessions/", requestOptions).then(
      (data) => data.data as PractiseSession[]
    );
  }

  static async postPractiseSession(topicId: number) {
    const requestOptions: RequestInit = {
      method: "POST",
      body: JSON.stringify({ topicId: topicId }),
    };
    return (await this._fetchAPI(
      "practisesessions/",
      requestOptions
    )) as PractiseSession;
  }

  static async deletePractiseSessions(practiseSessionId: number) {
    const requestOptions: RequestInit = {
      method: "DELETE",
    };
    return await this._fetchAPI(
      `practisesession/${practiseSessionId}`,
      requestOptions
    );
  }

  static async getSessionCardsPractiseSession(practiseSessionId: number) {
    const requestOptions: RequestInit = {
      method: "GET",
    };
    return await this._fetchAPI(
      `sessioncards/${practiseSessionId}`,
      requestOptions
    ).then((data) => data.data as SessionCard[]);
  }

  static async putSessionCard(sessionCardId: number, correct: boolean) {
    const requestOptions: RequestInit = {
      method: "PUT",
      body: JSON.stringify({ correct: correct }),
    };
    return await this._fetchAPI(`sessioncard/${sessionCardId}`, requestOptions);
  }
}

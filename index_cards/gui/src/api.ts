import { Card, Topic } from "./models";
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
      requestOptions.mode = "same-origin";
      return requestOptions;
    }
    if (requestOptions.method !== "POST" && requestOptions.method !== "PUT") {
      return requestOptions;
    }
    if (!csrftoken || !csrftoken.csrftoken) {
      console.log("CSRF Error thrown");
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
      .then((response) => response.json());
  }

  static async getTopics(): Promise<[Topic | any]> {
    const requestOptions: RequestInit = {
      method: "GET",
      mode: "same-origin",
    };
    return await this._fetchAPI("topics/", requestOptions).then(
      (data) => data.data
    );
  }

  static async getTopic(id: number): Promise<Topic | any> {
    const requestOptions: RequestInit = {
      method: "GET",
      mode: "same-origin",
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions).then(
      (data) => data.data
    );
  }

  static async putTopic(id: number, topicName: string): Promise<Topic> {
    const requestOptions: RequestInit = {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic_name: topicName }),
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
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topicName: topicName }),
    };
    return await this._fetchAPI("topics/", requestOptions);
  }

  static async getCards(): Promise<[Card]> {
    const requestOptions: RequestInit = {
      method: "GET",
      mode: "same-origin",
    };
    return await this._fetchAPI("cards/", requestOptions).then(
      (data) => data.data
    );
  }

  static async getCard(id: number): Promise<Card> {
    const requestOptions: RequestInit = {
      method: "GET",
      mode: "same-origin",
    };
    return await this._fetchAPI(`card/${id}`, requestOptions).then(
      (data) => data.data
    );
  }

  static async putCard(
    id: number,
    topic?: number,
    question?: string,
    answer?: string
  ): Promise<Card | any> {
    if (!topic && !question && !answer) {
      return;
    }
    let body = { topic: topic, question: question, answer: answer };
    let card: any;
    if (!topic || !question || !answer) {
      card = await this.getCard(id);
    }
    if (!question) {
      body.question = card.question;
    }
    if (!answer) {
    }
    if (!topic) {
    }
    const requestOptions: RequestInit = {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions);
  }

  static async deleteCard(id: number) {
    const requestOptions: RequestInit = {
      method: "DELETE",
    };
    return await this._fetchAPI(`topic/${id}`, requestOptions);
  }

  static async postCard(topicName: string) {
    const requestOptions: RequestInit = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic_name: topicName }),
    };
    return await this._fetchAPI("topics/", requestOptions);
  }
}

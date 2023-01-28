export default class APIInterface {
  static baseUrl = new URL("http://localhost:8000/");

  static async getTopics() {
    const requestOptions = {
      method: "GET",
      mode: "same-origin",
    };
    const data = await fetch(new URL("api/topics/", this.baseUrl))
      .then((response) => response.json())
      .then((data) => data.data)
      .catch((error) => console.log(error));
    console.log(data);
  }
}

import { authenticatedGetRequestOption } from "./helpers/networkCall";
import { handleResponse } from "./helpers/handleResponse";
import {URL} from "./helpers/envinronment"

const getMovieList = () => {
    return fetch(`${URL}/get_movie_list`, authenticatedGetRequestOption())
      .then(handleResponse)
      .then((classroom) => {
        return classroom;
      })
  };

export default getMovieList
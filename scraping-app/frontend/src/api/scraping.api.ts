import axios from "axios";

export const scrape = async () => {
  return axios.get("http://localhost:8000/api/scrape");
};
export const getAllProducts = async () => {
  return axios.get("http://localhost:8000/api/products/");
};

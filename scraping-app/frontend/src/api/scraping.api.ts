import axios from "axios";
type SearchData = {
  genero: string;
  prenda: string;
};
export const scrape = async (data: SearchData) => {
  // return axios.get("http://localhost:8000/api/scrape");
  return axios.get("http://localhost:8000/api/scrape", {
    params: {
      genero: data.genero,
      prenda: data.prenda,
    },
  });
};
export const getAllProducts = async () => {
  return axios.get("http://localhost:8000/api/products/");
};
export const getFilterProducts = async (
  min_price?: number,
  max_price?: number,
  color?: string
) => {
  return axios.get("http://localhost:8000/api/products/filter", {
    params: {
      min_price: min_price,
      max_price: max_price,
      color: color,
    },
  });
};

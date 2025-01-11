import axios from "axios";
export const getColor = async (rgb: string) => {
  return axios.get(
    `https://www.thecolorapi.com/id?format=svg&rgb=rgb${rgb}&named=false`
  );
};

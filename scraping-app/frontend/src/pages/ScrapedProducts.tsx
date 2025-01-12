import { useEffect, useState } from "react";
import { getAllProducts, getFilterProducts } from "../api/scraping.api";
import { Image } from "@nextui-org/image";
import { filter } from "framer-motion/client";
interface Product {
  id: number;
  name: string;
  price: number;
  url: string;
  images: Image[];
  colors: Color[];
}
interface Image {
  id: number;
  url: string;
}
interface Color {
  id: number;
  name: string;
  rgb: string;
}
function ScrapedProducts() {
  const [data, setData] = useState([]);
  const [filters, setFilters] = useState({
    min_price: 0,
    max_price: 0,
    color: "",
  });
  const loadProducts = async () => {
    const response =
      filters.min_price !== 0 || filters.max_price !== 0 || filters.color !== ""
        ? await getFilterProducts(
            filters.min_price,
            filters.max_price,
            filters.color
          )
        : await getAllProducts();
    if (response.status !== 200) {
      console.log("Error");
      return;
    }
    setData(response.data);
  };
  const handleFiltersSearch = async () => {
    console.log(filters);
    const response = await getFilterProducts(
      filters.min_price === 0 ? undefined : filters.min_price,
      filters.max_price === 0 ? undefined : filters.max_price,
      filters.color
    );
    console.log(response);
    if (response.status !== 200) {
      console.log("Error");
      return;
    }
    setData(response.data.products);
  };
  useEffect(() => {
    loadProducts();
  }, []);
  return (
    <>
      <div className="flex gap-4">
        <article className="flex flex-col gap-4 p-4 bg-white rounded-lg shadow-md">
          <div className="flex flex-col gap-2">
            <label htmlFor="min_price" className="font-semibold text-gray-700">
              Precio minimo
            </label>
            <input
              id="min_price"
              type="number"
              className="p-2 border border-gray-300 rounded-md"
              value={filters.min_price}
              onChange={(e) =>
                setFilters({ ...filters, min_price: Number(e.target.value) })
              }
            />
          </div>
          <div className="flex flex-col gap-2">
            <label htmlFor="max_price" className="font-semibold text-gray-700">
              Precio Maximo
            </label>
            <input
              id="max_price"
              type="number"
              className="p-2 border border-gray-300 rounded-md"
              value={filters.max_price}
              onChange={(e) =>
                setFilters({ ...filters, max_price: Number(e.target.value) })
              }
            />
          </div>
          <div className="flex flex-col gap-2">
            <label htmlFor="color" className="font-semibold text-gray-700">
              Color
            </label>
            <input
              id="color"
              type="text"
              className="p-2 border border-gray-300 rounded-md"
              value={filters.color}
              onChange={(e) =>
                setFilters({ ...filters, color: e.target.value })
              }
            />
          </div>
        </article>
        <button onClick={handleFiltersSearch}>Buscar</button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {
          <h2>
            Filtros aplicados: {filters.color} {filters.min_price}{" "}
            {filters.max_price}
          </h2>
        }
        {data.map((product: Product) => (
          <a
            key={product.id}
            className="rounded-xl shadow-md p-4 flex flex-col items-center gap-4"
            href={product.url}
            target="_blank"
          >
            <div>{product.name}</div>
            <div>{product.price}</div>
            {/* <div>{product.url}</div> */}
            <div className="flex gap-2 flex-wrap">
              {product.images.map((image: Image) => (
                <Image
                  key={image.id}
                  src={image.url}
                  width={150}
                  isZoomed
                  isBlurred
                ></Image>
              ))}
            </div>
            <div className="rounded-xl shadow-md px-6 py-2">
              {product.colors.map((color: Color, i: number) => (
                <div className="flex items-center gap-2" key={color.id}>
                  <div>{color.name}</div>
                  <img
                    className="rounded-full h-2 w-2"
                    src={`https://www.thecolorapi.com/id?format=svg&rgb=rgb${color.rgb}&named=false`}
                  ></img>
                </div>
              ))}
            </div>
          </a>
        ))}
      </div>
    </>
  );
}

export default ScrapedProducts;

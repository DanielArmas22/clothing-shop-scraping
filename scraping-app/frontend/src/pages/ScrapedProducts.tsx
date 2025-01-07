import { useEffect, useState } from "react";
import { getAllProducts } from "../api/scraping.api";

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
}
function ScrapedProducts() {
  const [data, setData] = useState([]);
  const loadProducts = async () => {
    const response = await getAllProducts();
    if (response.data.length > 0) {
      setData(response.data);
    } else {
      console.log("No data found");
    }
  };
  useEffect(() => {
    loadProducts();
  }, []);
  return (
    <div className="grid grid-cols-3 gap-4">
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
          <div>
            {product.images.map((image: Image) => (
              <img key={image.id} src={image.url}></img>
            ))}
          </div>
          <div>
            {product.colors.map((color: Color) => (
              <img key={color.id} src={color.name}></img>
            ))}
          </div>
        </a>
      ))}
    </div>
  );
}

export default ScrapedProducts;

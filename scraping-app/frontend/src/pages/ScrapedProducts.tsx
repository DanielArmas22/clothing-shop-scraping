import { useEffect, useState } from "react";
import { getAllProducts } from "../api/scraping.api";
import { getColor } from "../api/colors.api";
import { set } from "react-hook-form";
import { Image } from "@nextui-org/image";
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
  const [colores, setcolores] = useState([]);
  const loadProducts = async () => {
    const response = await getAllProducts();
    console.log(response.data);
    // setColorcito(colorcito.data);
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
      {/* <div dangerouslySetInnerHTML={{ __html: colorcito }} /> */}
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
            {product.colors.map((color: Color) => (
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
  );
}

export default ScrapedProducts;

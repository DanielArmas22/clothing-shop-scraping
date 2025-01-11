import { useEffect, useState } from "react";
import { getAllProducts, getFilterProducts } from "../api/scraping.api";
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
interface Props {
  min_price: number;
  max_price: number;
}
function ScrapedProducts(props: Props) {
  const [data, setData] = useState([]);
  const loadProducts = async () => {
    const response =
      props.min_price && props.max_price
        ? await getFilterProducts(props.min_price, props.max_price)
        : await getAllProducts();
    if (response.status !== 200) {
      console.log("Error");
      return;
    }
    setData(response.data);
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

import { useEffect, useState } from "react";
import { getAllProducts } from "../api/scraping.api";

interface Product {
  id: number;
  name: string;
  price: number;
  url: string;
  images: Image[];
}
interface Image {
  id: number;
  url: string;
}
function Home() {
  const [data, setData] = useState([]);
  const loadProducts = async () => {
    const response = await getAllProducts();
    setData(response.data);
  };
  useEffect(() => {
    loadProducts();
  }, []);
  return (
    <>
      <div className="text-3xl">Home</div>
      <h3></h3>
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
          </a>
        ))}
      </div>
    </>
  );
}

export default Home;

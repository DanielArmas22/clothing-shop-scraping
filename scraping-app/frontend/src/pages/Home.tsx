import ScrapedProducts from "./ScrapedProducts";
import { useState } from "react";
import SearchForScrap from "./SearchForScrap";
function Home() {
  const [isClicked, setIsClicked] = useState(false);
  const handleShowAllProductsButton = () => {
    setIsClicked(!isClicked);
  };

  return (
    <>
      <div className="text-3xl">Home</div>
      <div className="my-32"></div>
      <button
        onClick={handleShowAllProductsButton}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Mostrar Todos los productos
      </button>
      {isClicked && <ScrapedProducts />}
      <br></br>
      <br />
      <SearchForScrap />
    </>
  );
}

export default Home;

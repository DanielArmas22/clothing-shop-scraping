// import React from "react";
import { useForm, SubmitHandler } from "react-hook-form";
type FormData = {
  genero: string;
  prenda: string;
};
function SearchForScrap() {
  const { register, handleSubmit } = useForm<FormData>();
  const onSubmit: SubmitHandler<FormData> = (data, e) => {
    e?.preventDefault();
    console.log(data);
  };
  return (
    <>
      <div></div>
      <form
        action="GET"
        onSubmit={handleSubmit(onSubmit)}
        className="space-y-4 p-4 bg-gray-100 rounded-md shadow-md"
      >
        <div>
          <label
            htmlFor="genero"
            className="block text-sm font-medium text-gray-700"
          >
            Genero
          </label>
          <input
            id="genero"
            type="text"
            {...register("genero", { required: true })}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          />
        </div>
        <div>
          <label
            htmlFor="prenda"
            className="block text-sm font-medium text-gray-700"
          >
            Prenda
          </label>
          <input
            id="prenda"
            type="text"
            {...register("prenda", { required: true })}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          />
        </div>
        <button
          type="submit"
          className="mt-4 w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Submit
        </button>
      </form>
    </>
  );
}

export default SearchForScrap;

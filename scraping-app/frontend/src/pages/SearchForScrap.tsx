// import React from "react";
import { useForm } from "react-hook-form";
function SearchForScrap() {
  const { register } = useForm();
  const handleSubmit = (data: any) => {
    console.log(data);
  };
  return (
    <>
      <div></div>
      <form action="GET"></form>
    </>
  );
}

export default SearchForScrap;

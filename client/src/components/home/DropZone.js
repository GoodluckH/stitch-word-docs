import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import axios from "axios";
import Cookies from "js-cookie";

const DropZone = () => {
  const onDrop = useCallback((acceptedFiles) => {
    // Do something
    console.log(acceptedFiles);
    const csrftoken = Cookies.get("csrftoken");
    var form_data = new FormData();
    for (var i = 0; i < acceptedFiles.length; i++) {
      form_data.append("atw", acceptedFiles[i]);
    }

    axios
      .post("http://127.0.0.1:8000/upload/", form_data, {
        header: {
          "content-type": "undefined",
          "X-CSRFToken": csrftoken,
        },
      })
      .then((res) => {})
      .catch((e) => console.log(e));
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Drop the files here ...</p>
      ) : (
        <p>Drag 'n' drop some files here, or click to select files</p>
      )}
    </div>
  );
};

export default DropZone;

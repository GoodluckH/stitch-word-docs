import React, { useCallback, useMemo } from "react";
import { useDropzone } from "react-dropzone";
import axios from "axios";
import Cookies from "js-cookie";

import "./DropZone.css";

const baseStyle = {
  display: "flex",
  width: "70%",
  height: "100%",
  minHeight: "500px",
  minWidth: "300px",
  maxWidth: "1200px",
  maxHeight: "1000px",
  margin: "10px",
  justifyContent: "center",
  flexDirection: "column",
  alignItems: "center",
  padding: "20px",
  borderWidth: 10,
  borderRadius: 5,
  borderColor: "#eeeeee",
  borderStyle: "dashed",
  backgroundColor: "#fafafa",
  color: "#bdbdbd",
  outline: "none",
  transition: "border .24s ease-in-out",
};

const activeStyle = {
  borderColor: "#2196f3",
};

const DropZone = () => {
  const onDrop = useCallback((acceptedFiles) => {
    // Do something
    const csrftoken = Cookies.get("csrftoken");
    var form_data = new FormData();
    for (var i = 0; i < acceptedFiles.length; i++) {
      form_data.append("atw", acceptedFiles[i]);
    }

    axios
      .post("https://atw.herokuapp.com/upload/", form_data, {
        header: {
          "content-type": "undefined",
          "X-CSRFToken": csrftoken,
        },
      })
      .then((res) => {
        window.open("https://atw.herokuapp.com/download/");
      })
      .catch((e) => console.log(e));
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  const style = useMemo(
    () => ({
      ...baseStyle,
      ...(isDragActive ? activeStyle : {}),
    }),
    [isDragActive]
  );
  return (
    <div className="dropZone">
      <div {...getRootProps({ style })}>
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Drop the files here ...</p>
        ) : (
          <p>
            Drag 'n' drop Around the World files here, or click to select files
          </p>
        )}
      </div>
    </div>
  );
};

export default DropZone;

import { useState } from "react";

const CreateArticle = () => {
    const [formData, setFormData] = useState({
      name: "",
      desc: "",
      type: "",
      size: "",
      gender: "",
      state: "",
      image: "",
    });
  
    const [message, setMessage] = useState("");
  
    // Fonction pour mettre à jour les champs du formulaire
    const handleChange = (e) => {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    };
  
    // Fonction pour envoyer le formulaire
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      try {
        const response = await fetch("http://127.0.0.1:8000/api/create_article/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        //   credentials: "include", // Permet d'envoyer les cookies d'authentification
        });
  
        const data = await response.json();
  
        if (response.ok) {
          setMessage("Article créé avec succès !");
          setFormData({ name: "", desc: "", type: "", size: "", gender: "", state: "", image: "" });
        } else {
          setMessage(data.message || "Erreur lors de la création de l'article");
        }
      } catch (error) {
        console.error("Erreur :", error);
        setMessage("Erreur de connexion au serveur");
      }
    };
  
    return (
      <div>
        <h2>Créer un nouvel article</h2>
        {message && <p>{message}</p>}
        <form onSubmit={handleSubmit}>
          <input type="text" name="name" placeholder="Nom" value={formData.name} onChange={handleChange} required />
          <input type="text" name="desc" placeholder="Description" value={formData.desc} onChange={handleChange} />
          <input type="text" name="type" placeholder="Type" value={formData.type} onChange={handleChange} />
          <input type="text" name="size" placeholder="Taille" value={formData.size} onChange={handleChange} />
          <input type="text" name="gender" placeholder="Genre" value={formData.gender} onChange={handleChange} />
          <input type="text" name="state" placeholder="État" value={formData.state} onChange={handleChange} />
          <input type="text" name="image" placeholder="URL de l'image" value={formData.image} onChange={handleChange} />
  
          <button type="submit">Créer l'article</button>
        </form>
      </div>
    );
  };
  
  export default CreateArticle;
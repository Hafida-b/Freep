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
          Nom :   
          <input type="text" name="name" placeholder="Nom" value={formData.name} onChange={handleChange} required />
          <br />
          Description :   
          <input type="text" name="desc" placeholder="Description" value={formData.desc} onChange={handleChange} />
          <br />
          {/* <input type="text" name="type" placeholder="Type" value={formData.type} onChange={handleChange} /> */}
          <label>
            Type :
            <select name="type" value={formData.type} onChange={handleChange}>
              <option value="Hauts">Hauts</option>
              <option value="Accessoires">Accessoires</option>
              <option value="Bas">Bas</option>
              <option value="Vêtements de soirée">Vêtements de soirée</option>
              <option value="Déguisement">Déguisement</option>
              <option value="Vêtements de sport">Vêtements de sport</option>
            </select>
           </label>

           <br />
          {/* <input type="text" name="size" placeholder="Taille" value={formData.size} onChange={handleChange} /> */}
          <label>
            Taille :
            <select name="size" value={formData.size} onChange={handleChange}>
              <option value="XS">XS</option>
              <option value="S">S</option>
              <option value="M">M</option>
              <option value="L">L</option>
              <option value="XL">XL</option>
              <option value="XXL">XXL</option>
            </select>
          </label>
          <br />

          {/* <input type="text" name="gender" placeholder="Genre" value={formData.gender} onChange={handleChange} /> */}
          <label>
            Genre :
            <select name="gender" value={formData.gender} onChange={handleChange}>
              <option value="Femme">Femme</option>
              <option value="Homme">Homme</option>
              <option value="Unisex">Unisexe</option>
            </select>
          </label>
          <br />

          {/* <input type="text" name="state" placeholder="État" value={formData.state} onChange={handleChange} /> */}
          <label>
            État :
            <select name="state" value={formData.state} onChange={handleChange}>
              <option value="Neuf">Neuf</option>
              <option value="Comme Neuf">Comme Neuf</option>
              <option value="Très bon état">Très bon état</option>
              <option value="Bon état">Bon état</option>
              <option value="Usé">Usé</option>
              <option value="Abimé">Abimé</option>
            </select>
          </label>
          <br />
          Image : 
          <input type="text" name="image" placeholder="URL de l'image" value={formData.image} onChange={handleChange} /><br />
  
          <button type="submit">Créer l'article</button>
        </form>
      </div>
    );
  };
  
  export default CreateArticle;
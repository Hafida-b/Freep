import { Link } from "react-router-dom";

function Navigation() {
  return (
    <nav>
      <Link to="/">Accueil</Link>
      <Link to="/signup">S'inscrire</Link>
      <Link to="/login">Se connecter</Link>
      <Link to="/create">Créer un article</Link>
      <Link to="/articles">Liste des articles</Link>
    </nav>
  );
}
export default Navigation;
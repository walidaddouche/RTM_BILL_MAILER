<h1>Gestion des factures RTM</h1>

<p>Ce script vous permet de gérer vos factures RTM de manière automatisée. Il vous permet de récupérer la liste de vos factures, de télécharger les factures au format PDF et de les envoyer par email.</p>

<h2>Comment utiliser ce script</h2>

<p>Voici les étapes à suivre pour utiliser ce script :</p>

<ol>
  <li>Instanciez la classe <code>RtmClient</code> dans votre script.</li>
  <li>Appelez la méthode <code>login</code> de l'instance de <code>RtmClient</code>. Cette méthode tentera de se connecter à l'API RTM en utilisant l'email et le mot de passe stockés dans les variables d'environnement. Si la connexion échoue, la méthode renverra <code>False</code>.</li>
  <li>Si la connexion a réussi, vous pouvez appeler la méthode <code>get_all_bills</code> pour récupérer la liste des factures de l'utilisateur. Cette méthode renverra un tableau de dictionnaires, chaque dictionnaire représentant une facture.</li>
  <li>Pour télécharger une facture en PDF, appelez la méthode <code>get_bill_by_id</code> en lui passant en paramètre l'identifiant unique de la facture que vous souhaitez télécharger. Cette méthode renverra l'URL de la facture en PDF.</li>
  <li>Pour envoyer la facture par email, vous pouvez utiliser n'importe quelle bibliothèque de gestion des emails, comme <code>smtplib</code> ou <code>email</code> de Python.</li>
</ol>

<h2>Exemple d'utilisation</h2>

<p>Voici un exemple de script qui utilise les fonctionnalités de <code>RtmClient</code> pour
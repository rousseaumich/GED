# settings.py
AUTH_LDAP_SERVER_URI = 'ldap://your-ldap-server.com'# Cette ligne spécifie l'URI du serveur LDAP ou Active Directory que votre application Django utilisera pour l'authentification. Remplacez 'ldap://your-ldap-server.com' par l'adresse de votre serveur Active Directory.

AUTH_LDAP_BIND_DN = 'cn=admin,dc=your-domain,dc=com' # Le AUTH_LDAP_BIND_DN est le Distinguished Name (DN) du compte utilisé pour se connecter au serveur LDAP. Dans cet exemple, 'cn=admin,dc=your-domain,dc=com' indique que le compte administrateur a un Common Name (cn) de "admin" et appartient au domaine "your-domain.com". Remplacez cette valeur par le DN approprié pour votre configuration Active Directory.
AUTH_LDAP_BIND_PASSWORD = 'your-password'
#Cette ligne spécifie le mot de passe du compte utilisé pour se connecter au serveur LDAP. Remplacez 'your-password' par le mot de passe réel du compte administrateur.
AUTH_LDAP_USER_DN_TEMPLATE = 'cn={username},dc=your-domain,dc=com'
#Le AUTH_LDAP_USER_DN_TEMPLATE définit le modèle de Distinguished Name (DN) utilisé pour construire le DN d'un utilisateur à partir de son nom d'utilisateur. Dans cet exemple, 'cn={username},dc=your-domain,dc=com' indique que le DN d'un utilisateur aura un Common Name (cn) égal à son nom d'utilisateur et appartiendra au domaine "your-domain.com". Assurez-vous que ce modèle correspond à la structure de votre Active Directory.
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=people,dc=your-domain,dc=com', ldap.SLACK_SEARCH)
# Le AUTH_LDAP_USER_SEARCH définit la recherche LDAP utilisée pour trouver un utilisateur par son nom d'utilisateur. Dans cet exemple, 'ou=people,dc=your-domain,dc=com' indique que les utilisateurs sont stockés dans l'unité organisationnelle (OU) "people" du domaine "your-domain.com". Ajustez cette valeur en fonction de l'emplacement réel des utilisateurs dans votre Active Directory.

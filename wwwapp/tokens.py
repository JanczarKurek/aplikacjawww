from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):

    @staticmethod
    def _make_hash_value(user, timestamp):
        return (
            f"{user.pk}{timestamp}{user.is_active}"
        )


account_activation_token = TokenGenerator()

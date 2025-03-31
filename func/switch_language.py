def switch_language(screen, buttons_settings, buttons_settings_rect, language):
    if language == "rus":
        screen.blit(buttons_settings[0], buttons_settings_rect[0])
        screen.blit(buttons_settings[1], buttons_settings_rect[1])
        screen.blit(buttons_settings[3], buttons_settings_rect[3])
        screen.blit(buttons_settings[4], buttons_settings_rect[4])
        screen.blit(buttons_settings[5], buttons_settings_rect[5])
        screen.blit(buttons_settings[6], buttons_settings_rect[6])
        screen.blit(buttons_settings[7], buttons_settings_rect[7])
        screen.blit(buttons_settings[9], buttons_settings_rect[9])
    elif language == "eng":
        screen.blit(buttons_settings[0], buttons_settings_rect[0])
        screen.blit(buttons_settings[1], buttons_settings_rect[1])
        screen.blit(buttons_settings[3], buttons_settings_rect[3])
        screen.blit(buttons_settings[4], buttons_settings_rect[4])
        screen.blit(buttons_settings[5], buttons_settings_rect[5])
        screen.blit(buttons_settings[6], buttons_settings_rect[6])
        screen.blit(buttons_settings[7], buttons_settings_rect[7])
        screen.blit(buttons_settings[9], buttons_settings_rect[9])

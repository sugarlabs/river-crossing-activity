import pygame

def scale_image_maintain_ratio(img, w = None, h = None):
    o_w, o_h = img.get_size()
    m_w, m_h = o_w, o_h

    if w is not None and h is None:
        m_h = w * (o_h / o_w)
        return pygame.transform.scale(img, (int(w), int(m_h)))
        
    if h is not None and w is None:
        m_w = h * (o_w / o_h)
        return pygame.transform.scale(img, (int(m_w), int(h)))
    
    if w is None and h is None:
        return img

def array_has_no_none(arr):
    return all(element is not None for element in arr)


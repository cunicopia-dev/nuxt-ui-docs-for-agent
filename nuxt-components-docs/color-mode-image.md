<!-- source: https://ui.nuxt.com/components/color-mode-image --> # ColorModeImagePRO

[GitHub](https://github.com/nuxt/ui-pro/blob/v3/src/runtime/components/color-
mode/ColorModeImage.vue)

An image element with a different source for light and dark mode.

## Usage

The ColorModeImage component uses the `<NuxtImg>` component when
[`@nuxt/image`](https://github.com/nuxt/image) is installed, falling back to
`img` otherwise.

light

dark

![](https://picsum.photos/id/29/400)![](https://picsum.photos/id/46/400)

    
    
    <template>
      <UColorModeImage
        light="https://picsum.photos/id/29/400"
        dark="https://picsum.photos/id/46/400"
        :width="200"
        :height="200"
      />
    </template>
    

Switch between light and dark mode to see the different images: System

## API

### Props

Prop |  Default |  Type   
---|---|---  
`light`| | `string`  
`dark`| | `string`  
  
[ColorModeButtonA Button to switch between light and dark
mode.](/components/color-mode-button)[ColorModeSelectA Select to switch
between system, dark & light mode.](/components/color-mode-select)


<!-- source: https://ui.nuxt.com/components/color-mode-avatar --> # ColorModeAvatarPRO

[Avatar](/components/avatar)[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/color-mode/ColorModeAvatar.vue)

An Avatar with a different source for light and dark mode.

## Usage

The ColorModeAvatar component extends the [Avatar](/components/avatar)
component, so you can pass any property such as `size`, `icon`, etc.

Use the `light` and `dark` props to define the source for light and dark mode.

light

dark

![](https://github.com/vuejs.png)![](https://github.com/nuxt.png)

    
    
    <template>
      <UColorModeAvatar light="https://github.com/vuejs.png" dark="https://github.com/nuxt.png" />
    </template>
    

Switch between light and dark mode to see the different images: System

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'span'`| `any`The element or component this component should render as.  
`light`| | `string`  
`dark`| | `string`  
`icon`| | ` string`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`  
`alt`| | ` string`  
`text`| | ` string`  
`ui`| | ` { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`  
  
[CollapsibleA collapsible element to toggle visibility of its
content.](/components/collapsible)[ColorModeButtonA Button to switch between
light and dark mode.](/components/color-mode-button)


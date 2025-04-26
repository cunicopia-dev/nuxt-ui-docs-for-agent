<!-- source: https://ui.nuxt.com/components/color-mode-button --> # ColorModeButtonPRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/color-mode/ColorModeButton.vue)

A Button to switch between light and dark mode.

## Usage

The ColorModeButton component extends the [Button](/components/button)
component, so you can pass any property such as `color`, `variant`, `size`,
etc.

    
    
    <template>
      <UColorModeButton />
    </template>
    

The button defaults to `color="neutral"` and `variant="ghost"`.

## Examples

### With custom icons

Use the `app.config.ts` to customize the icon with the `ui.icons` property:

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        icons: {
          light: 'i-ph-sun',
          dark: 'i-ph-moon'
        }
      }
    })
    

Use the `vite.config.ts` to customize the icon with the `ui.icons` property:

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            icons: {
              light: 'i-ph-sun',
              dark: 'i-ph-moon'
            }
          }
        })
      ]
    })
    

### With fallback slot

As the button is wrapped in a
[ClientOnly](https://nuxt.com/docs/api/components/client-only) component, you
can pass a `fallback` slot to display a placeholder while the component is
loading.

    
    
    <template>
      <UColorModeButton>
        <template #fallback>
          <UButton loading variant="ghost" color="neutral" />
        </template>
      </UColorModeButton>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'button'`| `any`The element or component this component should render
as when not a link.  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'ghost'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`disabled`| | `boolean`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`ui`| | ` { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`fallback`| `{}`  
  
[ColorModeAvatarAn Avatar with a different source for light and dark
mode.](/components/color-mode-avatar)[ColorModeImageAn image element with a
different source for light and dark mode.](/components/color-mode-image)

